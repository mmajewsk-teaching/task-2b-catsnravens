
# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

import json
from pathlib import Path
from statistics import mean

#data structures

#dict_students = {
#    "student1": {"name": "Ala", "surname": "Makota",
#        "grades": {"Math": [5, 2], "Biology": [4, 1]},
#        "attendance": [0, 1, 1, 1, 0]},
#
#    "student2": {"name": "Wiktoria", "surname": "Niemakota",
#        "grades": {"Math": [4, 5], "Biology": [5, 5]},
#        "attendance": [1, 1, 1, 1, 0]},
#
#    "student3": {"name": "Katarzyna", "surname": "Kot",
#        "grades": {"Math": [4, 4], "Biology": [3, 5], "Physics": [4, 3]},
#        "attendance": [1, 1, 1, 1, 1]},
#
#    "student4": {"name": "Jan", "surname": "Kowalski",
#        "grades": {"Math": [2, 3], "Biology": [4, 2], "Physics": [3, 4]},
#        "attendance": [1, 0, 1, 1, 1]},
#
#    "student5": {"name": "Anna", "surname": "Kowalska",
#        "grades": {"Math": [5, 5], "Biology": [5, 4], "Physics": [4, 5]},
#        "attendance": [1, 1, 1, 0, 1]},
#
#    "student6": {"name": "Adam", "surname": "Nowak",
#        "grades": {"Math": [3, 4], "Physics": [3, 2]},
#        "attendance": [1, 1, 0, 1, 1]},
#
#    "student7": {"name": "Ewa", "surname": "Cicha",
#        "grades": {"Math": [4, 5], "Biology": [5, 5], "Physics": [5, 4]},
#        "attendance": [1, 1, 1, 1, 1]},
#
#    "student8": {"name": "Piotr", "surname": "Cichy",
#        "grades": {"Math": [2, 2], "Biology": [3, 2], "Physics": [3, 3]},
#        "attendance": [0, 1, 1, 0, 1]},
#
#    "student9": {"name": "Dominik", "surname": "Popel",
#        "grades": {"Math": [5, 4], "Biology": [4, 4], "Physics": [4, 5]},
#        "attendance": [1, 1, 0, 1, 1]},
#
#    "student10": {"name": "Tomasz", "surname": "Karp",
#        "grades": {"Math": [3, 5], "Biology": [5, 3], "Physics": [3, 4]},
#        "attendance": [1, 1, 1, 1, 0]},
#
#    "student11": {"name": "Alicja", "surname": "Jagla",
#        "grades": {"Computer Science": [5, 4], "Python": [4, 5]},
#        "attendance": [1, 0, 1, 1, 1]},
#
#    "student12": {"name": "Krzysztof", "surname": "Kryk",
#        "grades": {"Computer Science": [5, 5], "Python": [4, 4], "Chemistry": [5, 5]},
#        "attendance": [0, 0, 0, 0, 0]},
#
#    "student13": {"name": "Piotr", "surname": "Zimny",
#        "grades": {"Computer Science": [4, 3], "Python": [3, 4], "Chemistry": [4, 3]},
#        "attendance": [1, 1, 1, 1, 1]},
#
#    "student14": {"name": "Dawid", "surname": "Prezydent",
#        "grades": {"Computer Science": [4, 5], "Chemistry": [5, 4]},
#        "attendance": [1, 1, 1, 0, 1]},
#
#    "student15": {"name": "Marta", "surname": "Krawa",
#        "grades": {"Computer Science": [3, 2], "Chemistry": [3, 2]},
#        "attendance": [1, 1, 0, 1, 0]},
#
#    "student16": {"name": "Zofia", "surname": "Data",
#        "grades": {"Computer Science": [5, 4], "Chemistry": [4, 5]},
#        "attendance": [1, 1, 1, 1, 1]},
#
#    "student17": {"name": "Olga", "surname": "Borek",
#        "grades": {"Computer Science": [4, 4], "Chemistry": [5, 5]},
#        "attendance": [1, 0, 1, 1, 1]},
#
#    "student18": {"name": "Jakub", "surname": "Bagnet",
#        "grades": {"Computer Science": [3, 5], "Python": [4, 4], "Chemistry": [4, 3]},
#        "attendance": [1, 1, 1, 1, 0]},
#
#    "student19": {"name": "Łukasz", "surname": "Kowalczyk",
#        "grades": {"Computer Science": [5, 5], "Python": [5, 4], "Chemistry": [5, 4]},
#        "attendance": [1, 1, 1, 1, 1]},
#
#    "student20": {"name": "Bartosz", "surname": "Babel",
#        "grades": {"Computer Science": [2, 3], "Python": [3, 2], "Chemistry": [3, 3]},
#        "attendance": [1, 0, 0, 0, 0]}
#}



dict_schools = {
    "Highschool 1": [f"student{i}" for i in range(1, 11)],   # 1 - 10
    "Highschool 2": [f"student{i}" for i in range(11, 21)]   # 11 - 20
}

dict_courses = {
    "Math": {
        "teacher": "Mr. Math",
        "students": [f"student{i}" for i in range(1, 11)]
    },
    "Biology": {
        "teacher": "Mrs. Bio",
        "students": [f"student{i}" for i in list(range(1,6)) + list(range(7,11))]
    },
    "Physics": {
        "teacher": "Mr. Phys",
        "students": [f"student{i}" for i in range(3, 11)]
    },
    "Computer Science": {
        "teacher": "Mrs. CS",
        "students": [f"student{i}" for i in range(11, 21)]
    },
    "Python": {
        "teacher": "Mr. M",
        "students": [f"student{i}" for i in list(range(11,14)) + list(range(18,21))]
    },
    "Chemistry": {
        "teacher": "Mrs. Chem",
        "students": [f"student{i}" for i in range(12, 21)]
    }
}

# writing & reading files (2)

def read_data(filename="school_data.json"):
    p = Path(filename)
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except Exception:
        print("Error reading data from file")
        return None
        
def write_data(data, filename="school_data.json"):
    Path(filename).write_text(json.dumps(data, indent=2, ensure_ascii=False))

#averages (4)
def student_average(student):
    grades = []
    for subject in student["grades"]:
        grades.extend(student["grades"][subject])
    if  not grades:
        return None
    return mean(grades) 


def course_average(subject):
    grades = []
    for student in dict_students.values():
        if subject in student.get("grades", {}):
            grades.extend(student["grades"][subject])
    if not grades:
        return None
    return mean(grades)

def school_average_course(school, subject):
    grades = []
    for student_key in dict_schools.get(school, []):
        student = dict_students.get(student_key, {})
        if subject in student.get("grades", {}):
            for grade in student["grades"][subject]:
                grades.append(grade)
    if not grades:
        return None
    return mean(grades)

def school_average(school):
    grades = []
    for student_key in dict_schools.get(school, []):
        student = dict_students.get(student_key, {})
        for subject in student.get("grades", {}):
            for grade in student["grades"][subject]:
                grades.append(grade)
    if not grades:
        return None
    return mean(grades)

#other functions (1-4)  <11

def attendance(student):
    return sum(student["attendance"])/ len(student["attendance"])

#use of MAP and LAMBDA (functional programming)
def print_student_info(student):
    print(student["name"] + " " + student["surname"])
    print("Grades:")
    grades_list = list(map(lambda sub: f"{sub}: {student['grades'][sub]}", student["grades"]))
    for line in grades_list:
        print("  " + line)
    print("Attendance: " + str(attendance(student) * 100) + " %")


def add(what, student, value):
    if what == "grade":
        subject, grade = value
        student["grades"].setdefault(subject, []).append(grade)
    elif what == "attendance":
        student["attendance"].append(value)


if __name__ == "__main__":

    dict_students = read_data("students.json")
    if dict_students == None:
        print("Failed to load student data\n")
        exit(1)

    print(f"Average grade for {dict_students["student1"]["name"]} {dict_students["student1"]["surname"]} for all courses:", student_average(dict_students["student1"]))
    print(f"Average grade for {dict_students["student3"]["name"]} {dict_students["student3"]["surname"]} for all courses:", student_average(dict_students["student3"]), "\n")

    print("Math average for all students in the course:", course_average("Math"))
    print("Physics average for all students in the course:", course_average("Physics"), "\n")

    print("Highschool 1 overall average:", school_average("Highschool 1"))
    print("Highschool 2 Computer Science average:", school_average_course("Highschool 2", "Computer Science"), "\n")

    print(f"Attendance for {dict_students["student1"]["name"]} {dict_students["student1"]["surname"]}:", attendance(dict_students["student1"]))
    print(f"Attendance for {dict_students["student7"]["name"]} {dict_students["student7"]["surname"]}:", attendance(dict_students["student7"]), "\n")
    print("Student nr 1 info:")
    print_student_info(dict_students["student1"])
    print()
    print("Student nr 2 info:")
    print_student_info(dict_students["student2"])
    print()

    add("grade", dict_students["student1"], ("Math", 5))
    add("attendance", dict_students["student1"], 1)
    print("Student nr 1 info modified:")
    print_student_info(dict_students["student1"])
    print()

    write_data(dict_students, "students1.json")



