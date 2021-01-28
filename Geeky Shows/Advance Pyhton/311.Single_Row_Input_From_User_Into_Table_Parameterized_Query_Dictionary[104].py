# Insert Single Row Input From User Dictionary
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
# Data Input From User
nm=input('Enter Name:')
ro=int(input('Enter Roll:'))
fe=float(input('Enter Fees:'))
params={'name':nm,'roll':ro,'fees':fe}
try:
    myc.execute(sql,params)
    conn.commit()   # Commiting The Changes
    print('Total Rows:',myc.rowcount)   # Number Of Row Inserted
    print(f'Stu ID: {myc.lastrowid} Inserted')   # Last Inserted ID
except:
    conn.rollback() # Rollback The Changes
    print('Unable To Insert Data')
myc.close() # Close Cursor
conn.close()    # Close Connection