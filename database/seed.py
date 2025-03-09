from sqlalchemy.orm import Session
from database.db import SessionLocal
from database.models import Group, Student, Teacher, Subject, Grade
from faker import Faker
import random
import datetime

fake = Faker()

def seed_database():
    session = SessionLocal()
    
    # Очистимо таблиці перед заповненням
    session.query(Grade).delete()
    session.query(Student).delete()
    session.query(Group).delete()
    session.query(Subject).delete()
    session.query(Teacher).delete()
    session.commit()
    
    # Створюємо викладачів (гарантуємо, що викладач id=1 існує)
    teacher_1 = Teacher(id=1, name=fake.name())
    session.add(teacher_1)
    session.commit()
    
    other_teachers = [Teacher(name=fake.name()) for _ in range(4)]
    session.add_all(other_teachers)
    session.commit()
    all_teachers = [teacher_1] + other_teachers
    
    # Створюємо групи
    groups = [Group(name=f"Group {i+1}") for i in range(3)]
    session.add_all(groups)
    session.commit()
    
    # Створюємо предмети (гарантуємо, що викладач id=1 має хоча б один предмет)
    subjects = [Subject(name=fake.word(), teacher=teacher_1)]
    for _ in range(7):
        subjects.append(Subject(name=fake.word(), teacher=random.choice(all_teachers)))
    session.add_all(subjects)
    session.commit()
    
    # Гарантовано додаємо студентів у кожну групу
    students = []
    for group in groups:
        num_students = random.randint(10, 20)  # Хоча б 10 студентів у групі
        for _ in range(num_students):
            student = Student(name=fake.name(), group=group)
            students.append(student)
    session.add_all(students)
    session.commit()
    
    # Додаємо оцінки студентам (гарантовано додаємо оцінки з предмета викладача id=1)
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(10, 20)):
                grade = Grade(
                    student=student,
                    subject=subject,
                    grade=random.randint(60, 100),
                    date_received=fake.date_between(start_date="-1y", end_date="today")
                )
                session.add(grade)
    
    session.commit()
    session.close()
    print("Database reseeded successfully!")

if __name__ == "__main__":
    seed_database()