class Student:
    n = 0;

    def __init__(self):
        Student.n = Student.n+1;

    @staticmethod
    def detyails():
        print("number of students is ",Student.n);

s1 = Student();
s1.detyails();

    
