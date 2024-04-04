from sqlalchemy import func, desc
from schema import *

engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')
DBSession = sessionmaker(bind=engine)
session = DBSession()


def select_1():
    return session.query(Student.name, func.round(func.avg(ScoreRecord.score)).label('avg_score')) \
        .select_from(ScoreRecord).join(Student).group_by(Student.id).order_by(desc('avg_score')).limit(5).all()


def select_2(subject_name):
    return session.query(Student.name, Subject.title, func.round(func.avg(ScoreRecord.score)).label('avg_score')) \
        .select_from(ScoreRecord).join(Student).join(Subject).filter(Subject.title == subject_name) \
        .group_by(Student.id, Subject.title).order_by(desc('avg_score')).limit(1).all()


def select_3(subject_name):
    return session.query(Group.name, Subject.title, func.round(func.avg(ScoreRecord.score)).label('avg_score')) \
        .select_from(ScoreRecord).join(Student).join(Group).join(Subject).filter(Subject.title == subject_name) \
        .group_by(Group.id, Subject.title).order_by(desc('avg_score')).all()


def select_4():
    return session.query(func.round(func.avg(ScoreRecord.score))) \
        .select_from(ScoreRecord).all()


def select_5(professor_name):
    return session.query(Subject.title) \
        .select_from(Professor).join(Subject).filter(Professor.name == professor_name).all()


def select_6(group_id):
    return session.query(Student.name) \
        .select_from(Student).join(Group).filter(Group.id == group_id).all()


def select_7(subject_title, group_id):
    return session.query(Student.name, Student.group_id, ScoreRecord.score) \
        .select_from(ScoreRecord).join(Student).join(Subject).filter(Subject.title == subject_title) \
        .filter(Student.group_id == group_id).all()


def select_8(professor_name):
    return session.query(func.round(func.avg(ScoreRecord.score))) \
        .select_from(ScoreRecord).join(Subject).join(Professor).filter(Professor.name == professor_name).all()


def select_9(student_id):
    return session.query(Subject.title) \
        .select_from(ScoreRecord).join(Subject).filter(ScoreRecord.student_id == student_id).all()


def select_10(student_id, professor_id):
    return session.query(Subject.title) \
        .select_from(ScoreRecord).join(Subject).filter(ScoreRecord.student_id == student_id) \
        .filter(Subject.professor_id == professor_id).all()


def select_11(student_name, professor_name):
    return session.query(func.round(func.avg(ScoreRecord.score))) \
        .select_from(ScoreRecord).join(Subject).join(Professor).join(Student) \
        .filter(Professor.name == professor_name) \
        .filter(Student.name == student_name).all()


def select_12(subject_title, group_id):
    subquery = session.query(func.max(ScoreRecord.date)).scalar_subquery()
    return session.query(Student.name, ScoreRecord.score, ScoreRecord.date) \
        .select_from(ScoreRecord).join(Student).join(Subject) \
        .filter(Subject.title == subject_title) \
        .filter(Student.group_id == group_id) \
        .filter(ScoreRecord.date == subquery) \
        .all()


# .filter(ScoreRecord.date == subquery.c.max_date)

def print_result(text, result):
    print(f"{text}:\n{result}\n\n")


def main():
    print_result("Top 5 Students with Highest Average Grade", select_1())
    print_result("Student with Highest Average Grade in Specific Subject", select_2('Pharmacologist'))
    print_result("Average Grade in Groups for Specific Subject", select_3('Pharmacologist'))
    print_result("Average Grade in All Subjects", select_4())
    print_result("Courses Taught by Specific Teacher", select_5('Scott Cordova'))
    print_result("List of Students in Specific Group", select_6(25))
    print_result("Grades of Students in Specific Group for Specific Subject", select_7('Pharmacologist', 25))
    print_result("Average Grade Given by Specific Teacher for Their Subjects", select_8('Scott Cordova'))
    print_result("List of Courses Attended by Specific Student", select_9(130))
    print_result("Courses Taught by Specific Teacher to Specific Student", select_10(117, 44))
    print_result("Average Grade Given by Specific Teacher to Specific Student",
                 select_11('Patricia Le', 'Albert Hinton'))
    print_result("Grades of Students in Specific Group for Specific Subject on Last Class",
                 select_12('Pharmacologist', 25))


if __name__ == '__main__':
    main()
