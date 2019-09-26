import mysql.connector;

from mysql.connector import Error;

print("establishing connection..");

try:
    con = mysql.connector.connect(host = "localhost",database = "student",user = "root",password = "");

    print("established connection..",con);


    querycreat = "create table stud2(";
    querycreat = querycreat + " roll int not null,name varchar(25) not null, semester int not null , gender boolean not null,p_marks int not null,php_marks int not null,j_marks int not null)";
    

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
