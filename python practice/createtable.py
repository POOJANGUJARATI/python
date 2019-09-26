import mysql.connector;

from mysql.connector import Error;

print("establishing connection..");

try:
    con = mysql.connector.connect(host = "localhost",database = "mydb",user = "root",password = "");

    print("established connection..",con);


    querycreat = "create table person(";
    querycreat = querycreat + "name varchar(25) not null,age int not null)";

    print(querycreat);

    cursor = con.cursor();
    cursor.execute(querycreat);

    con.commit();
    print("table is created.");
    

except Error as e:
    print("error while connecting..",e);


finally:
    if(con.is_connected()):
        cursor.close();
        con.close();
    
    
