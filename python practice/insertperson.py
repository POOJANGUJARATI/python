import mysql.connector;

from mysql.connector import Error;

print("establishing connection..");

try:
    con = mysql.connector.connect(host = "localhost",database = "student",user = "root",password = "");

    print("established connection..",con);


    stdroll = input("enter a student roll to be inserted in table:");
    stdnm = input("enter a student name to be inserted in table:");
    sem = input("enter a semester to be inserted in table:");
    stdgen = input("enter a student gender[F/M]: to be inserted in table:");
    if(stdgen=="MALE" or  stdgen=="male"):
        gender = "1";
    else:
        gender = "0";
    stdpy_marks = input("enter a python marks to be inserted in table:");
    stdphp_marks = input("enter a php marks to be inserted in table:");
    stdjava_marks = input("enter a java marks to be inserted:");
    
    

    queryinsert = "insert into stud2 values(";
    queryinsert = queryinsert + stdroll + ",";
    queryinsert = queryinsert + "'"+ stdnm + "',";
    queryinsert = queryinsert + sem + ","; 
    queryinsert = queryinsert + "'"+gender + "',";
    queryinsert = queryinsert + stdpy_marks + ",";
    queryinsert = queryinsert + stdphp_marks + ",";
    queryinsert = queryinsert + stdjava_marks + ")";
        

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
