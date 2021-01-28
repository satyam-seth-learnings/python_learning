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
sql1='INSERT INTO student(name,roll,fees) VALUES("Ram",105,85647.5)'
sql2='INSERT INTO student(name,roll,fees) VALUES("Aman",106,15615),("Rakesh",107,16556.7),("Pinki",108,94612.8)'
myc=conn.cursor()
try:
    myc.execute(sql1)   #Or myc.execute(sql2)
    conn.commit()
    print(myc.rowcount,'Row Inserted')
except:
    conn.rollback()
    print('Unable To Insert Data')
myc.close()
conn.close()