class String:
    
   # def __init__(self):
    #    print(" default constructor is called..");

    
    def __init__(self,st =""):
        print("parametersid constructor is called..");
        self.str = st;     

    def  set(self,st = ""):
        self.str = st;

    def get(self):
       return self.str;

    def stringlength(self):
        return len(self.str);
        #return self.strlen;

    def joinstr(self,str2):
        self.str = self.str+str2.str;
        
    
    def comparestring(self,str2):
        if self.str==str2:
            return True;
        else:
            return False;

    def revstring(self):
        return self.str[::-1];

    def palindrome(self):
        self.revst = self.str[::-1];
        if self.str == self.revst:
            print("string is palindrome :");
        else:
            print("string is not palindrome:");
            
    def checkwordin(self,str2):
        self.strtt = self.str.find(str2.str);
        return self.strtt;

    
s1 = String();
s1.set("poojan");
s2= String();
s2.set("gujarati");
print("s1= ",s1.get());
print("s1=",s1.set());

print("s1= length of the string",s1.stringlength());
print("s1= joining of string is:",s1.joinstr(s2));


print("s1= comparing of string =",s1.comparestring(s2));


print("s1 = reversing a string =",s1.revstring());
print("s1 = check palindrome string",s1.palindrome());

print("s1 = check word in the string = ",s1.checkwordin(s2));
