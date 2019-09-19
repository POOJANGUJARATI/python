class String:
    def __init__(self,st=""):
        print("\n Constructor Calling....");
        self.str=st;
        
    def set(self,st=""):
        self.str=st;
        
    def get(self):
        return self.str;

    def length(self):
        length=len(self.str);
        print("\n Length : ",length);

    def join(self,String_object):
        self.str=self.str+String_object.str;
        print("\n Joining String : ",self.str);
        
    def compare(self,str1):
        if self.str==str1.str:
            return True;
        else:
            return False;
        
    def reverse(self):
        length=len(self.str);
        for i in range(1,length+1):
            reve=self.str[::-1];
        print("\n Reverse : ",reve);

    def check_palindrome(self):
        rev = self.reverse();
        if(self.str == rev):
            return True;
        else:
            return False;

    def word_present(self,str1):
        self.str1=str1;
        n=self.str.find(self.str1,0,len(self.str));
        if n==-1:
            print("\n Word not found");
        else:
             print("\n Word found at position : ",n+1);       
            
s1=String("ddu");
print("\n String-1 : ",s1.get());
s1.length();

s2=String("ddu");
print("\n string-2 : ",s2.get());
s2.length();

#s1.join(s2);

print("s1 =",s1.get(), "s2 =",s2.get());
if(s1.compare(s2)):
    print("s1 and s2 are same.");
else:
    print("s1 and s2 are different.");
s1.reverse();
s1.set("dduudd");
if(s1.check_palindrome()):
    print("s1 is palindrome.");
else:
    print("s1 is not palindrome.");
    

