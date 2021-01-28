print("{:,}".format(1234567890))
print("{:_}".format(1234567890))
name="Rahul"
age=62
print("My Name Is {} And Age Is {}".format(name,age))
a=50
b=3
print("{:.2}".format(a/b))
print("{:.2%}".format(a/b))
print("Accessing Arguments Items")
value=(10,20)
print("{0[0]} {0[1]}".format(value))
data={'Rahul':2000,"Sonam":3000}
print("{0[Rahul]} {0[Sonam]}".format(data))
print("{d[Rahul]} {d[Sonam]}".format(d=data))
print("{Rahul} {Sonam}".format(**data))