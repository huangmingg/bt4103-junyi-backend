import time
import logging
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extras import RealDictCursor
from internal.config.config import get_env_config
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session

logger = logging.getLogger(__name__)


class PostgreSqlBase:
    _pool = None

    def __init__(self):
        self._load_config()
        if self.config:
            self._validate_database()
            self._pool = SimpleConnectionPool(**self.config)
            self._db = self.session_factory()

    @property
    def db(self) -> Session:
        return self._db

    def cleanup(self, exception=None):
        if exception:
            self.db.rollback()
            return
        self.db.commit()

    def ping(self):
        return self._get_alive_connection()

    def fetch_row(self, query, params={}):
        conn = self._get_alive_connection()
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            row = cur.fetchone()
            print(row)
            if row:
                col_names = map(lambda item: item[0], cur.description)
                data = dict(zip(col_names, row))
                return data
            return None
        finally:
            if conn:
                self._pool.putconn(conn)

    def fetch_rows(self, query, params={}):
        conn = self._get_alive_connection()
        try:
            cur = conn.cursor(cursor_factory=RealDictCursor)
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            rows = cur.fetchall()
            if rows:
                arr = []
                for row in rows:
                    arr.append(dict(row))
                return arr
            return None
        except Exception as e:
            raise Exception("Fail to fetch from database")
        finally:
            if conn:
                self._pool.putconn(conn)

    def exec_transaction(self, query, param={}):
        conn = self._get_alive_connection()
        try:
            cur = conn.cursor()
            cur.execute(query, param)
            conn.commit()
            return True
        except Exception as e:
            raise Exception("Database transaction fail.")
        finally:
            if conn:
                self._pool.putconn(conn)

    def _load_config(self):
        try:
            self.config = get_env_config()['database']
        except Exception as e:
            logger.error(e)
            raise Exception(e)

    def _validate_database(self):
        self.engine = create_engine(f"postgres://{self.config['user']}:{self.config['password']}@{self.config['host']}/{self.config['database']}")
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        self.session_factory = scoped_session(sessionmaker(bind=self.engine))

    def _get_alive_connection(self):
        max_retry_count = 10
        while True:
            conn = None
            try:
                conn = self._pool.getconn()
                cursor = conn.cursor()
                cursor.execute('SELECT 1')
                cursor.fetchall()
                conn.commit()
                return conn
            except Exception as e:
                logger.error(f"Fail to fetch from database - {e}")
                time.sleep(1)
                if conn:
                    self._pool.putconn(conn)
                max_retry_count -= 1
                if max_retry_count <= 0:
                    raise Exception("Maximum retries reached")

    def close_connection(self):
        conn = self._get_alive_connection()
        if conn:
            self._pool.putconn(conn)


db_instance = PostgreSqlBase()
