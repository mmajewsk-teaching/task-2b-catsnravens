import json
from pathlib import Path
from statistics import mean

#data structures
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

#other functions (3)  sum = 9 functions total is in 7-10 range

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



