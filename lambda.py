
mul = lambda x,y : x*y

result = mul(10,20);
print("MULTIPLICATION IS :",result);

div = lambda x,y : x//y

result = div(25,2);
print("DIVISION IS :",result);

lst = [3,10,7,20];
list1 = list(filter(lambda x:(x%2 ==0),lst));
print("even number is :",list1);

lst = [3,10,7,20];
list1 = list(filter(lambda x:(x%2 ==1),lst));
print("odd number is :",list1);
