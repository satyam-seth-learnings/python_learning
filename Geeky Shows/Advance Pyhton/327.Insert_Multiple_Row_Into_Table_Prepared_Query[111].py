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
sql='INSERT INTO student(name,roll,fees) VALUES(?,?,?)' #Or sql='INSERT INTO student(name,roll,fees) VALUES(%s,%s,%s)'
myc=conn.cursor(prepared=True)
seq_of_params=[
        ('Niti',222,48646.7),
        ('Himesh',333,74844.4),
        ('Arijit',444,96521)]
try:
    myc.executemany(sql,seq_of_params)
    conn.commit()   # Commiting The Changes
    print('Rows Inserted')
except:
    conn.rollback() # Rollback The Changes
    print('Unable To Insert Data')
myc.close() # Close Cursor
conn.close()    # Close Connection