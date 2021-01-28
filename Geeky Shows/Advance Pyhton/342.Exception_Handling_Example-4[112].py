a=10
b=0 #Or b=5
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print('Division by Zero Not Allowed')
else:
    print('Inside Else')
finally:
    print('Inside Finally')
print('Rest Of The Code')