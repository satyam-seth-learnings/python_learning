# Insert Multiple Row Input From User Dictionary
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
    sql='INSERT INTO student(name,roll,fees) VALUES(%(name)s,%(roll)s,%(fees)s)'
    myc=conn.cursor()
    n=nm
    r=ro
    f=fe
    params={'name':n,'roll':r,'fees':f}
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
while True:
    # Data Input From User
    nm=input('Enter Name:')
    ro=int(input('Enter Roll:'))
    fe=float(input('Enter Fees:'))
    student_data(nm,ro,fe)
    ans=input('Do You Want To Exit?(y/n):')
    if ans=='y':
        break