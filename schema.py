from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Mapped, sessionmaker, DeclarativeBase, mapped_column
from datetime import datetime


engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Base(DeclarativeBase):
    pass


class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'))


class Subject(Base):
    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    professor_id: Mapped[int] = mapped_column(ForeignKey('professors.id'))


class Professor(Base):
    __tablename__ = 'professors'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]


class ScoreRecord(Base):
    __tablename__ = 'score_records'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.id'))
    score: Mapped[int]
    date: Mapped[datetime]


Base.metadata.create_all(engine)
Base.metadata.bind = engine

