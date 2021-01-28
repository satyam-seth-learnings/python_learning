class Myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s='Provide At Least Two Numbers'
        return s
obj=Myclass()
print(obj.sum())
print(obj.sum(10))
print(obj.sum(10,20))
print(obj.sum(11,20,30))



# class Myclass:
#     def sum(self,a=None,b=None,*args):
#         if a==None or b==None:
#             s='Provide At Least Two Numbers'
#         else:
#             s=a+b
#             if args:
#                 for i in args:
#                     s+=i
#         return s
# obj=Myclass()
# print(obj.sum())
# print(obj.sum(10))
# print(obj.sum(10,20))
# print(obj.sum(11,20,30))
# print(obj.sum(11,20,30,40))
# print(obj.sum(11,20,30,40,50))