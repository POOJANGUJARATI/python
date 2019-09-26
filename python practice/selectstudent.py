import mysql.connector;
from mysql.connector import Error;

print("establishing connection..");

try:
    con = mysql.connector.connect(host = "localhost",database = "student",user = "root",password = "");

    print("established connection..",con);

    queryselect = "select *from stud2";
    print(queryselect);

    cursor = con.cursor();
    cursor.execute(queryselect);
    result = cursor.fetchall();
    con.commit();

    print("total number of rows in emp:",cursor.rowcount);
    print("fetching detalis..\n");

    for row in result:
        if(row[3] == 1):
            gender = "male";
        else:
            gender = "female";
        print("\trolll:",row[0]);
        print("\tname:",row[1]);
        print("\tsgender:",gender);

    print("selection succsessfully..");

except Error as e:
    print("connecting error :",e);

finally:
    if(con.is_connected()):
        cursor.close();
        con.close();
        
