# DictWriter
from csv import DictWriter
with open('File4.csv','w',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['firstname','lastname'])
    csv_writer.writeheader()
    csv_writer.writerow({'firstname':'harshit','lastname':'dixit'})
    csv_writer.writerow({'firstname':'satyam','lastname':'seth'})
    csv_writer.writerows([{'firstname':'Harshit','lastname':'Dixit'},{'firstname':'Satyam','lastname':'seth'}])