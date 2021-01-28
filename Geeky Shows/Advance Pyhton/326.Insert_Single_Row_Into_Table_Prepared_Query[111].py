# Insert Single Row
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
sql='INSERT INTO student(name,roll,fees) VALUES(%s,%s,%s)'  #Or sql='INSERT INTO student(name,roll,fees) VALUES(?,?,?)'
myc=conn.cursor(prepared=True)
params=('Kishan',177,34980.50)
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