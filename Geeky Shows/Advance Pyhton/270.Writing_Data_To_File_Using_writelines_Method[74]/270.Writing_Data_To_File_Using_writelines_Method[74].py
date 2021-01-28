f=open('student.txt',mode='w')
lst1=['Rahul','Sonam ','Sumit','Raj']
f.writelines(lst1)
f.close()
print('Success')
lst2=['\nRahul\n','Sonam\n','Sumit\n','Raj']
f=open('student.txt',mode='a')
f.writelines(lst2)
f.close()
print('Updated')