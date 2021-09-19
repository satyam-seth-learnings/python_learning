# more about all() function
def my_sum(*args):
    if all([type(arg)==int or type(arg)==(float) for arg in args]):
        total=0
        for num in args:
            total+=num
        return total
    else:
        return "Worng Input"
print(my_sum(1,23,4.45,53.624))
print(my_sum(2,44.5,"Satyam",['name','age']))