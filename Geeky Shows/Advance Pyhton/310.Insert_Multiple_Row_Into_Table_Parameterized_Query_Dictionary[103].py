# Insert Multiple Row
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
sql='INSERT INTO student(name,roll,fees) VALUES(%(name)s,%(roll)s,%(fees)s)'
myc=conn.cursor()
params=[
    {'name':'Neha','roll':109,'fees':75361},
    {'name':'Ali','roll':110,'fees':48136},
    {'name':'Suraj','roll':111,'fees':45416}]
try:
    myc.executemany(sql,params)
    conn.commit()   # Commiting The Changes
    print('Total Rows:',myc.rowcount)   # Number Of Row Inserted
    print(f'Stu ID: {myc.lastrowid} Inserted')   # Last Inserted ID
except:
    conn.rollback() # Rollback The Changes
    print('Unable To Insert Data')
myc.close() # Close Cursor
conn.close()    # Close Connection