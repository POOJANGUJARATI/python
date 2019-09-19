import datetime;
class Person:
    x = datetime.datetime.now();
    current_Year = x.strftime("%Y");
    
    def  __init__(self,nm='',birthdate = datetime.datetime(2000,1,1),gen = ""):
        print("constructor is called");
        self.name=nm;
        self.birthdate=birthdate.strftime ("%d-%m-%Y");
        self.birthdate = datetime.datetime.strptime(self.birthdate,"%d-%m-%Y");
        self.year = self.birthdate.strftime("%Y");
        self.gender=gen;

    def set(self):
        self.name=input("Enter Name:");
        self.birthdate=input("Enter Date of Birth:");
        self.birthdate = datetime.datetime.strptime(self.birthdate,"%d-%m-%Y");
        self.year = self.birthdate.strftime("%Y");
        self.count_age();
        self.gender=input("Enter Gender : ");

    def count_age(self):
        self.age = int(Person.current_Year) - int(self.year);
        
        
    #def get(self):
     #   return self.gender;


    def show(self):
        print("person  name :",self.name);
        print("person birth date :",self.birthdate);
        print("student gender :",self.gender);
        print("student age :",self.age);
        print("student year :",self.year);
        

class Student(Person):
    def __init__(self):
        print("child constructor is called");
        super().__init__(name,gender);


    def set(self,sem,py_marks,j_marks,php_marks):
        self.sem = sem;
        self.py_marks = py_marks;
        self.j_marks = j_marks;
        self.php_marks = php_marks;


    def get(self):
        return self.sem,self.py_marks,self.j_marks,self.php_marks;

    
    def total(self):
        self.total = self.py_marks +self.j_marks + self.php_marks;
        self.perc = self.total/3;


    def show(self):
        super().show();
        print("student semester:",self.sem);
        print("student python marks",self.py_marks);
        print("student java marks",self.j_marks);
        print("student php marks:",self.php_marks);    
        print("total of subjects :",self.total);
        print("percentage of subjects:",self.perc);
        

class Employee(Person):

        def __init__(self,basic1_salary=0):
            super().__init__();
            print("Employee constructor is called");
            self.basic_salary = basic1_salary;

        def set(self):
            super().set();
            self.basic_salary = int(input("enter a salary:"));
            #self.dra = dra;
           # self.hra = hra;
            #self.total = total;

            
       # def get(self):
        #    return self.salary,self.dra,self.hra;
        

        def calc_da(self):
             if(self.gender)=='male' and (self.gender)=='Male':
                self.dan = (self.basic_salary*0.80);
             else:
                self.dan = (self.basic_salary*0.70);

            
        def calc_hra(self):
                if(self.gender)=='male' and (self.gender)=='Male':
                    self.hra = (self.basic_salary*0.10);
                else:
                    self.hra = (self.basic_salary*0.15);

        def gross_salary(self):
            self.grs = self.dan + self.hra + self.basic_salary;
            self.bons = self.basic_salary *0.50;
            self.gross = self.grs*12 + self.bons
            

        def show(self):
                super().show();
                print("basic salary:",self.basic_salary);
                print("dearness allowance:",self.dan);
                print("hra :",self.hra);
                print("total salary :", self.grs);
                print("bonus :",self.bons);
                print("gross salary :",self.gross);
                
        
        
    
e1 = Employee();
#e1.get();
e1.set();
e1.calc_da();
e1.calc_hra();
e1.gross_salary();
e1.show();
