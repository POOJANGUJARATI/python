rno = int(input("enter a roll number: "));
rname = str(input("enter a name of student: "));

m1 = int(input("enter a marks of sub1 :"));
m2 = int(input("enter a marks of sub2 :"));
m3 = int(input("enter a marks of sub3 :"));
m4 = int(input("enter a marks of sub4 :"));
ans = m1+m2+m3+m4;
print("summation of subjects :",ans);
per = (ans/400)*100;
print("percentage :",per);
#per = int(input("enter a percentage :"));

if  per<95 and per>80:
        print("grade A")

elif  per<82 and per>65:    
        print("grade B")

elif per<55 and per>10:
          print("grade c")

else :
        print("fail")
