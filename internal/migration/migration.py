from os import listdir
from os.path import isfile, join
import re
import logging

logger = logging.getLogger(__name__)

MIGRATION_TABLE_QUERY = """
	CREATE TABLE IF NOT EXISTS migration_metadata (
		"name" VARCHAR NOT NULL PRIMARY KEY
	);
	"""

CHECK_MIGRATION_QUERY = """
	SELECT 
		1
	FROM 
		INFORMATION_SCHEMA.TABLES
	WHERE 
		TABLE_TYPE='BASE TABLE' 
	AND
		TABLE_NAME='migration_metadata'
	"""

GET_MIGRATION_FILES_QUERY = """
	SELECT
		name
	FROM
		migration_metadata
	"""


def migrate_database(db_instance, migration_folder, is_migration_up=True):
    health_check = db_instance.ping()
    if not health_check:
        return
    init_metadata_table(db_instance)
    migrated_files = retrieve_migrated_file(db_instance)
    migration_files = retrieve_migration_file(migration_folder)
    return _migrate_up(db_instance, migrated_files, migration_files) if is_migration_up else _migrate_down(db_instance, migrated_files, migration_files)


def retrieve_migration_file(migration_folder, is_migration_up=True):
    files = [f for f in listdir(migration_folder) if isfile(join(migration_folder, f))]
    regex = "^[0-9]+-[a-zA-Z0-9\\s_.\\():]+[.]up[.]sql$" if is_migration_up else "^[0-9]+-[a-zA-Z0-9\\s_.\\():]+[.]down[.]sql$"
    output = []
    for file in files:
        if re.fullmatch(regex, file):
            direction = "up" if is_migration_up else "down"
            name = ', '.join(file.split(f".{direction}.sql")[:-1])
            output.append((name, join(migration_folder, file)))
    output.sort(key=lambda x: x[0])
    return output


def retrieve_migrated_file(db_instance):
    res = db_instance.fetch_rows(GET_MIGRATION_FILES_QUERY)
    return sorted([v['name'] for v in res]) if res else []


def init_metadata_table(db_instance):
    res = db_instance.fetch_row(CHECK_MIGRATION_QUERY)
    if not res:
        db_instance.exec_transaction(MIGRATION_TABLE_QUERY)


def _migrate_up(db_instance, migrated_files, migration_files):
    for n, p in migration_files:
        if n not in migrated_files:
            logger.info(f"executing migrating {n}")
            _execute_migration_file(db_instance, p)
            query = f"INSERT INTO migration_metadata VALUES ('{n}');"
            res = db_instance.exec_transaction(query)
            if not res:
                logging.error(f"Failed to execute migration metadata insertion for {n}")
    logging.info("migration files successfully executed")


def _migrate_down(db_instance, migrated_files, migration_files):
    pass


def _execute_migration_file(db_instance, file_path):
    with open(file_path, 'r', encoding='utf8') as migration_file:
        sql = migration_file.read()
        res = db_instance.exec_transaction(sql)
        if not res:
            logging.error(f"Failed to migrate file {file_path}")
    migration_file.close()

