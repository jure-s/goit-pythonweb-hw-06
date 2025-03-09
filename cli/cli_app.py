import argparse
from datetime import datetime
from database.db import SessionLocal
from database.models import Student, Group, Teacher, Subject, Grade

session = SessionLocal()

# --- Teacher Functions ---
def create_teacher(name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    print(f"Teacher '{name}' created successfully.")

def list_teachers():
    teachers = session.query(Teacher).all()
    for teacher in teachers:
        print(f"ID: {teacher.id}, Name: {teacher.name}")

def update_teacher(teacher_id, name):
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        teacher.name = name
        session.commit()
        print(f"Teacher ID {teacher_id} updated successfully.")
    else:
        print(f"Teacher ID {teacher_id} not found.")

def delete_teacher(teacher_id):
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"Teacher ID {teacher_id} deleted successfully.")
    else:
        print(f"Teacher ID {teacher_id} not found.")

# --- Student Functions ---
def create_student(name, group_id):
    student = Student(name=name, group_id=group_id)
    session.add(student)
    session.commit()
    print(f"Student '{name}' created successfully in Group ID {group_id}.")

def list_students():
    students = session.query(Student).all()
    for student in students:
        print(f"ID: {student.id}, Name: {student.name}, Group ID: {student.group_id}")

# --- Group Functions ---
def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    print(f"Group '{name}' created successfully.")

def list_groups():
    groups = session.query(Group).all()
    for group in groups:
        print(f"ID: {group.id}, Name: {group.name}")

# --- Subject Functions ---
def create_subject(name, teacher_id):
    subject = Subject(name=name, teacher_id=teacher_id)
    session.add(subject)
    session.commit()
    print(f"Subject '{name}' created successfully with Teacher ID {teacher_id}.")

def list_subjects():
    subjects = session.query(Subject).all()
    for subj in subjects:
        print(f"ID: {subj.id}, Name: {subj.name}, Teacher ID: {subj.teacher_id}")

# --- Grade Functions ---
def create_grade(student_id, subject_id, grade):
    new_grade = Grade(student_id=student_id, subject_id=subject_id, grade=grade, date_received=datetime.utcnow())
    session.add(new_grade)
    session.commit()
    print(f"Grade {grade} added for Student ID {student_id} in Subject ID {subject_id}.")

def list_grades(student_id=None):
    query = session.query(Grade)
    if student_id:
        query = query.filter(Grade.student_id == student_id)

    grades = query.all()
    for grade in grades:
        print(f"ID: {grade.id}, Student ID: {grade.student_id}, Subject ID: {grade.subject_id}, Grade: {grade.grade}, Date: {grade.date_received}")

# --- CLI Main Function ---
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"], required=True)
    parser.add_argument("-m", "--model", choices=["Teacher", "Student", "Group", "Subject", "Grade"], required=True)
    parser.add_argument("--id", type=int, help="ID of the record to update or remove")
    parser.add_argument("-n", "--name", type=str, help="Name for the record")
    parser.add_argument("-g", "--group_id", type=int, help="Group ID for students")
    parser.add_argument("-t", "--teacher_id", type=int, help="Teacher ID for subjects")
    parser.add_argument("-s", "--student_id", type=int, help="Student ID for grades")
    parser.add_argument("-sb", "--subject_id", type=int, help="Subject ID for grades")
    parser.add_argument("--grade", type=int, help="Grade value")

    args = parser.parse_args()

    if args.model == "Teacher":
        if args.action == "create" and args.name:
            create_teacher(args.name)
        elif args.action == "list":
            list_teachers()
        elif args.action == "update" and args.id and args.name:
            update_teacher(args.id, args.name)
        elif args.action == "remove" and args.id:
            delete_teacher(args.id)
        else:
            print("Invalid arguments for Teacher model.")

    elif args.model == "Student":
        if args.action == "create" and args.name and args.group_id:
            create_student(args.name, args.group_id)
        elif args.action == "list":
            list_students()
        else:
            print("Invalid arguments for Student model.")

    elif args.model == "Group":
        if args.action == "create" and args.name:
            create_group(args.name)
        elif args.action == "list":
            list_groups()
        else:
            print("Invalid arguments for Group model.")

    elif args.model == "Subject":
        if args.action == "create" and args.name and args.teacher_id:
            create_subject(args.name, args.teacher_id)
        elif args.action == "list":
            list_subjects()
        else:
            print("Invalid arguments for Subject model.")

    elif args.model == "Grade":
        if args.action == "create" and args.student_id and args.subject_id and args.grade:
            create_grade(args.student_id, args.subject_id, args.grade)
        elif args.action == "list":
            list_grades(args.student_id)
        else:
            print("Invalid arguments for Grade model.")

if __name__ == "__main__":
    main()
