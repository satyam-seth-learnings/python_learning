# Creating Table
import mysql.connector
try:
    conn=mysql.connector.connect(
        user='root',
        password='Seth7706',
        host='localhost',
        database='pdb',
        port=3306
    )
    if(conn.is_connected()):
        print('Connected')
except:
    print('Unable To Connect')
sql='CREATE TABLE student(stuid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20),roll INT,fees FLOAT)'
myc=conn.cursor()
myc.execute(sql)
myc.close()
conn.close()