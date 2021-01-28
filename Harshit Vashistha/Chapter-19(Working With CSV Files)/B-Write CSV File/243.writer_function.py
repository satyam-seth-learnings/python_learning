# writer function
from csv import writer
with open('File3.csv','w',newline='') as f:
    csv_writer=writer(f)
    # methods- writerow,writerows
    csv_writer.writerow(['name','countries'])  # csv_writer.writerows([['name','countries'],['harshit','INDIA'],['mohit','INDIA']])
    csv_writer.writerow(['harshit','INDIA'])    #
    csv_writer.writerow(['mohit','INDIA'])  #