# Creating Connection
import mysql.connector
config={
    'user':'root',
    'password':'Seth7706',
    'host':'localhost',
    'port':3306
}
try:
    conn=mysql.connector.connect(**config)
except:
    print('Unable To Connect')