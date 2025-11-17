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

class Student:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = { "Math" : 0,
                       "Biology" : 0}

    def print_info(self):
        print("Student: " + self.name + " " + self.surname)
        print ("Final grades ", self.grades)
    

    def add_grade(self, subject, grade):
        self.grades[subject] = grade
    

    def attendance(self):
        pass

class Class:
    def __init__(self):
        self.nr_of_people = 0
        self.students = []
    
    def add_student(self, Student):
        self.students.append(Student)
        self.nr_of_people += 1

    def class_average(self, subject):
        for student in self.students:
            grades += student.grades[subject]
        return grades/ self.nr_of_people



        


if __name__ == "__main__":

    print("The class:")
    student1 = Student("Ala", "Makota")
    student2 = Student("Katarzyna", "Niemakota")

    student1.print_info()
    student2.print_info()

    student1.add_grade("Math", 5)

    student1.print_info()

    myclass = Class()
    myclass.add_student(student1)
    myclass.add_student(student2)
    #print(myclass.class_average("Math"))




