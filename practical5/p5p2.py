class Person:
    
    def __init__(self,name,birthdate):
        self.name=name;
        self.birthdate=birthdate;

    @classmethod
    def set(cls,name,birthdate):
        cls.name=name;
        cls.birthdate=birthdate;

    @classmethod
    def get(cls):
        return (cls.name,cls.birthdate);
    
    def show(self):
        print("\n Name : ",self.name);
        print("\n Birthdate : ",self.birthdate);

p1=Person("shivani","7-12-1997");
p1.show();
Person.set("Shivu","25-06-1998");
print("\n Name and Birthdate : ",Person.get());

p2=Person("");
