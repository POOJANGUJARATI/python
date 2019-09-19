class Student:
    semester = 'sec'; # class variable
    
    def __init__(self,rno,rname,rage):
        self.number = rno;
        self.name = rname;
        self.age = rage;

    def getmethod(self):
        print("student roll number = ",self.number)
        print("student name is =",self.name);
        print("student age is=",self.age);
        

   
s1 = Student();
s1.getmethod();
s2 = Student();

print(s2.semester);
print(s1.semester); 
