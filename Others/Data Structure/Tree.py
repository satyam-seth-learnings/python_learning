l=[1,2,3,4,5,6,7,8,9,10]
n=int(input("Enter the Element:"))
ind=l.index(n)
try:
    def right(a):
        return l[a*2+2]
    def left(b):
        return l[b*2+1]
    def root(c):
        if c%2==0:
            return l[c//2-1]
        return l[c//2]
    print(f"Root:{root(ind)}\nLeft Child:{left(ind)}\nRight Child:{right(ind)}")
except:
    try:
        print(f"Root:{root(ind)}\nLeft Child:{left(ind)}\nRight Child:No")
    except:
        print(f"Root:{root(ind)}\nLeft Child:No\nRight Child:No")
        
