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
sql1='INSERT INTO student(name,roll,fees) VALUES("Rahul",109,41416.6)'
sql2='INSERT INTO student(name,roll,fees) VALUES("Suman",110,52595.9),("Himanshu",111,115416.7),("Anu",112,753985)'
myc=conn.cursor()
try:
    myc.execute(sql1)   #Or myc.execute(sql2)
    conn.commit()
    print('Student ID:',myc.lastrowid)
except:
    conn.rollback()
    print('Unable To Insert Data')
myc.close()
conn.close()