# Creating Connection
import mysql.connector
try:
    conn=mysql.connector.connect(
        user='root',
        password='Seth7707',
        host='localhost',
        port=3306
    )
except:
    print('Unable To Connect')