import mysql.connector;

from mysql.connector import Error;

print("establishing connection with mysql..");

try:
    con = mysql.connector.connect(host = "localhost",database = "mydb",user = "root",password = "");

    print("established connection..",con);

except Error as e:
    print("error while connecting:",e);


print("bye.");
    
