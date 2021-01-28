# Update Row - Dictionary
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
sql='UPDATE student SET name=%(nm)s,fees=%(fee)s WHERE stuid=%(id)s'
myc=conn.cursor()
update_value={'nm':'Iron Man','fee':700,'id':12}
try:
    myc.execute(sql,update_value)
    conn.commit()
    print(myc.rowcount,'Row Updated')
except:
    conn.rollback()
    print('Unable To Update Data')
myc.close()
conn.close()