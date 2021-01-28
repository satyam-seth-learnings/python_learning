price=1234568790
print(f"{price:,}")
print(f"{price:_}")
name="Rahul"
age=62
print(f"My name is {name} and age is {age}")
print("10*8")
print(f"{10*8}")
a,b=50,3
print(f"{a/b}")
print(f"{a/b:.2}")
print(f"{a/b:.2%}")
value=(10,20)
print(f"{value[0]} {value[1]}")
data={"Rahul":2000,"Sonam":3000}
print(f"{data['Rahul']:d} {data['Sonam']:d}")
cname="GeekyShows"
print(f"{cname.upper()}")
print(f"{10}")
print(f"{{10}}")
#Date And Time
from datetime import datetime
today=datetime(2019,10,5)
print(f"{today}")
print(f"{today:%d-%b-%Y}")
print(f"{today:%d/%b/%Y}")
print(f"{today:%d %b,%Y}")