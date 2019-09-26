import mysql.connector;

from mysql.connector import Error;

print("establishing connection..");

try:
    con = mysql.connector.connect(host = "localhost",database = "employee",user = "root",password = "");

    print("established connection..",con);


    querycreat = "create table emp(";
    querycreat = querycreat + " emp_number int not null,emp_name varchar(25) not null,gender boolean not null,b_date date not null,joining_date date not null,bas_salary int not null,da decimal(5,2),hra decimal(5,2) not null,net_salary decimal(5,2) not null)";
    

    print(querycreat);

    cursor = con.cursor();
    cursor.execute(querycreat);

    con.commit();
    print("table is created.");

except Error as e:
    print("error while connecting",e);

finally:
    if(con.is_connected()):
        cursor.close();
        con.close();
