from datetime import date
dob=date(1998,5,2)
t=date.today()
age=t.year-dob.year-((t.month,t.day)<(dob.month,dob.day))
print(age)