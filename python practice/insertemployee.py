import mysql.connector;

from mysql.connector import Error;

print("establishing connection..");

try:
    con = mysql.connector.connect(host = "localhost",database = "employee",user = "root",password = "");

    print("established connection..",con);


    empnumber  = input("enter a employee number to be inserted in table:");
    empname = input("enter a employee name to be inserted in table:");
    empgen = input("enter a employee gender to be inserted in table:");
    if(empgen=="male" or empgen=="MALE"):
        gender = "1";
    else:
        gender = "0";
    b_date = input("enter a employee birthdate to be inserted in table:");
    
    jn_date = input("enter a joining date to be inserted in table:");
    bas_salary = input("enter a basic salary to be inserted:");
    
    

    queryinsert = "insert into emp(emp_number,emp_name,gender,b_date,joining_date,bas_salary)values(";
    queryinsert = queryinsert + empnumber + ",";
    queryinsert = queryinsert + "'"+ empname + "',";
    queryinsert = queryinsert + "'"+ gender + "',";
    queryinsert = queryinsert +"'" +b_date + "',";
    queryinsert = queryinsert + "'"+jn_date + "',";
    queryinsert = queryinsert + bas_salary +")";
        

    print(queryinsert);

    cursor = con.cursor();
    cursor.execute(queryinsert);

    con.commit();
    print("inserted in table");

except Error as e:
    print("error while connecting",e);

finally:
    if(con.is_connected()):
        cursor.close();
        con.close();
