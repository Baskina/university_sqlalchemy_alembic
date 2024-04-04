import faker
from random import randint, choice
from schema import *

NUMBER_OF_STUDENTS = 50
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 5
NUMBER_OF_PROFESSORS = 5
NUMBER_OF_SCORE_RECORDS_PER_STUDENT_MAX = 20




def generate_fake_data(number_students, number_groups, number_subjects, number_professors, number_score_records):
    fake_students = []
    fake_groups = []
    fake_subjects = []
    fake_professors = []
    fake_score_records = []

    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_groups):
        fake_groups.append(fake_data.city())

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    for _ in range(number_professors):
        fake_professors.append(fake_data.name())

    for _ in range(number_score_records * number_students):
        fake_score_records.append(fake_data.random_int(0, 100))

    return fake_students, fake_groups, fake_subjects, fake_professors, fake_score_records


def prepare_data(students, groups, subjects, professors, score_records):
    student_data = []
    group_data = []
    subject_data = []
    professor_data = []
    score_record_data = []

    for group in groups:
        group_data.append(Group(name=group))

    for professor in professors:
        professor_data.append(Professor(name=professor))

    for student in students:
        student_data.append(Student(name=student, group_id=randint(25, 27)))

    for subject in subjects:
        subject_data.append(Subject(title=subject, professor_id=randint(41, 45)))


    for score_record in score_records:
        score_record_data.append(ScoreRecord(score=score_record,
                                             student_id=randint(101, 150),
                                             subject_id=randint(6, 10),
                                             date=choice(
                                                 [datetime(2024, 1, 1), datetime(2023, 1, 2), datetime(2022, 1, 3)])))

    return student_data, group_data, subject_data, professor_data, score_record_data


def insert_data_to_db(students, groups, subjects, professors, score_records):
    session.add_all(students)
    session.add_all(groups)
    session.add_all(subjects)
    session.add_all(professors)
    session.add_all(score_records)
    session.commit()


if __name__ == '__main__':
    students, groups, subjects, professors, score_records = prepare_data(
        *generate_fake_data(NUMBER_OF_STUDENTS, NUMBER_OF_GROUPS, NUMBER_OF_SUBJECTS, NUMBER_OF_PROFESSORS,
                            NUMBER_OF_SCORE_RECORDS_PER_STUDENT_MAX))

    insert_data_to_db(students, groups, subjects, professors, score_records)
