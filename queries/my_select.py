from sqlalchemy.orm import Session
from sqlalchemy import func
from database.models import Student, Grade, Subject, Teacher, Group
from database.db import SessionLocal

def select_1():
    """Знайти 5 студентів із найбільшим середнім балом."""
    session = SessionLocal()
    result = (
        session.query(Student.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
        .all()
    )
    session.close()
    return result

def select_2(subject_id: int):
    """Знайти студента з найвищим середнім балом з певного предмета."""
    session = SessionLocal()
    result = (
        session.query(Student.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(func.avg(Grade.grade).desc())
        .limit(1)
        .all()
    )
    session.close()
    return result

def select_3(subject_id: int):
    """Знайти середній бал у групах з певного предмета."""
    session = SessionLocal()
    result = (
        session.query(Group.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Student, Student.group_id == Group.id)  # Явно вказуємо зв'язок
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id, Group.name)  # Додаємо Group.name у group_by
        .all()
    )
    session.close()
    return result

def select_4():
    """Знайти середній бал на потоці."""
    session = SessionLocal()
    result = session.query(func.avg(Grade.grade)).scalar()
    session.close()
    return result

def select_5(teacher_id: int):
    """Знайти які курси читає певний викладач."""
    session = SessionLocal()
    result = (
        session.query(Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )
    session.close()
    return result

def select_6(group_id: int):
    """Знайти список студентів у певній групі."""
    session = SessionLocal()
    result = (
        session.query(Student.name)
        .filter(Student.group_id == group_id)
        .all()
    )
    session.close()
    return result

def select_7(group_id: int, subject_id: int):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    session = SessionLocal()
    result = (
        session.query(Student.name, Grade.grade)
        .join(Grade)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )
    session.close()
    return result

def select_8(teacher_id: int):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    session = SessionLocal()
    result = (
        session.query(func.avg(Grade.grade).label("avg_grade"))
        .join(Subject)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )
    session.close()
    return result

def select_9(student_id: int):
    """Знайти список курсів, які відвідує певний студент."""
    session = SessionLocal()
    result = (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )
    session.close()
    return result

def select_10(student_id: int, teacher_id: int):
    """Список курсів, які певному студенту читає певний викладач."""
    session = SessionLocal()
    result = (
        session.query(Subject.name)
        .join(Grade)
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)
        .distinct()
        .all()
    )
    session.close()
    return result