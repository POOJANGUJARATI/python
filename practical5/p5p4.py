import datetime;

class Person:
    
    def __init__(self):
        print("\n Constructor calling for Parent class....");

    def set(self,name,age,bdate,gender):
        self.name=name;
        self.age=age;
        self.bdate=bdate.strptime("%d-%m-%Y");
        self.bdate=datetime.datetime.strptime(self.bdate,"%d-%m-%Y");
        self.gender=gender;
        
    def get(self):
        return (self.name,self.age,self.bdate,self.gender);
    
    def show(self):
        print("Name : ",self.name);
        print("\n Age : ",self.age);
        print("Birthdate : ",self.bdate);
        print("\n Gender : ",self.gender);

class Student(Person):
    
    def __init__(self):
        print("Constructor calling for Student class....");

    def set(self,name,age,bdate,gender,semester,py_marks,j_marks,php_marks):
        super().set(name,age,bdate,gender);
        self.semester=semester;
        self.py_marks=py_marks;
        self.j_marks=j_marks;
        self.php_marks=php_marks;
        

    def get(self):
        return  Person.get(),self.semester,self.py_marks,self.j_marks,self.php_marks;

    def show(self):
        Person.show();
        print("\n Semester : ",self.semester);
        print("\n Python Marks : ",self.py_marks);
        print("\n Java Marks : ",self.j_marks);
        print("\n PHP Marks : ",self.php_marks);

    def calc_total(self):
        total=self.py_marks+self.j_marks+self.php_marks;
        return total;

    def calc_percentage(self):
        per=(self.calc_total()//3);
        
    def calc_grade(self):
        if self.calc_percentage() >= 70:
            return "A";
        elif self.calc_percentage() >=60:
            return "B";
        elif self.calc_percentage() >= 50:
            return "C";
        elif self.calc_percentage() >= 40:
            return "D";
        else:
            return "Fail";

class Employee(Person):

    def __init__(self):
        print("\n Constructor calling for Employee class....");

    def set(self,basic_sal,da,hra):
        Person.set(name,age,bdate,gender);
        self.basic_sal;
        self.da=da;
        self.hra=hra;

    def get(self):
        return Person.get(),self.basic_sal,self.da,self_hra;

    def show(self):
        Person.show();
        print("\n Basic Salary : ",self.basic_cal);
        print("\n DA : ",self.basic_da);
        print("\n HRA : ",self.hra);

    def calc_da(self):
        if gender=="male":
            self.da=self.basic_sal*.80;
            return self.da;
        else:
            self.da=self.basic_sal*.70;
            return self.da;
        
    def calc_hra(self):
        if gender=="male":
            self.hra=self.basic_sal*.10;
            return self.hra;
        else:
            self.hra=self.basic_sal*.15;
            return self.hra;
        
    def calc_total_sal(self):
        total=self.basic_sal+self.da+self.hra;
        return total;

    #def calc_gross_sal(self):
      #  gross_sal=self.basic_sal*.50
        

p1=Person();
p1.set("shivani",22,"1997-09-12","female");
p1.get();
p1.show();

s1=Student();
s1.set(3,88,77,66);
s1.get();
s1.show();

                        
        
