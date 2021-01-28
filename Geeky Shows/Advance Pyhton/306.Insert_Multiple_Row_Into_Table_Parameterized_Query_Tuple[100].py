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
sql='INSERT INTO student(name,roll,fees) VALUES(%s,%s,%s)'
myc=conn.cursor()
list_of_params=[('Jai',103,48646.7),('Veeru',104,74844.4),('Basanti',105,96521)]
try:
    myc.executemany(sql,list_of_params)
    conn.commit()   # Commiting The Changes
except:
    conn.rollback() # Rollback The Changes
    print('Unable To Insert Data')
myc.close() # Close Cursor
conn.close()    # Close Connection