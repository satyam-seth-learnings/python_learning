# Creating Connection
import mysql.connector
try:
    conn=mysql.connector.connect(
        user='root',
        password='Seth7706'
    )
    if(conn.is_connected()):
        print('Connected')
except:
    print('Unable To Connect')
print('Before Close:',conn.is_connected())
conn.close()
print('After Close:',conn.is_connected())