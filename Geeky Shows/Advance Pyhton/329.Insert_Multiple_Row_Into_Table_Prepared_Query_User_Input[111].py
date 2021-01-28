# Insert Multiple Row User Input
import mysql.connector
def student_data(nm,ro,fe):
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
    sql='INSERT INTO student(name,roll,fees) VALUES(?,?,?)' #Or sql='INSERT INTO student(name,roll,fees) VALUES(%s,%s,%s)'
    myc=conn.cursor(prepared=True)
    n=nm
    r=ro
    f=fe
    params=(n,r,f)
    try:
        myc.execute(sql,params)
        conn.commit()   # Commiting The Changes
        print('Row Inserted')
    except:
        conn.rollback() # Rollback The Changes
        print('Unable To Insert Data')
    myc.close() # Close Cursor
    conn.close()    # Close Connection
while True:
    # Data From User
    nm=input('Enter Name:')
    ro=int(input('Enter Roll:'))
    fe=float(input('Enter Fees:'))
    student_data(nm,ro,fe)
    ans=input('Do You Want To Exit(y/n)?:')
    if (ans=='y'):
        break