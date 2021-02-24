import datetime
from sqlalchemy import Column, DateTime, Integer, Text, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Text(), primary_key=True)
    name = Column(Text(), nullable=False)
    gender = Column(Text(), nullable=True)
    points = Column(Integer(), nullable=False)
    badges_cnt = Column(Integer(), nullable=False)
    first_login_date_TW = Column(Date(), nullable=False)
    user_grade = Column(Integer(), nullable=False)
    user_city = Column(Text(), nullable=True)
    is_self_coach = Column(Boolean(), nullable=False)
    belongs_to_class_cnt = Column(Integer(), nullable=False)
    has_class_cnt = Column(Integer(), nullable=False)
    has_teacher_cnt = Column(Integer(), nullable=False)
    has_student_cnt = Column(Integer(), nullable=False)
    created_by = Column(Text(), nullable=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)
    created_from = Column(Text(), nullable=False)
    updated_by = Column(Text(), nullable=False)
    updated_at = Column(DateTime(), nullable=False, default=datetime.datetime.utcnow)
    updated_from = Column(Text(), nullable=False)
    deleted_by = Column(Text(), nullable=True)
    deleted_at = Column(DateTime(), nullable=True)


class Content:
    pass


class Log:
    pass

