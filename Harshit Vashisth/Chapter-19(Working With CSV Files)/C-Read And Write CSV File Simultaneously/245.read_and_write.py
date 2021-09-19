from csv import DictReader,DictWriter
with open('File5.csv','r') as rf:
    with open('File6.csv','w',newline='') as wf:
        csv_reader=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=['first_name','last_name','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,lname,age=row['firstname'],row['lastname'],row['age']
            csv_writer.writerow({'first_name':fname.upper(),'last_name':lname.upper(),'age':age})