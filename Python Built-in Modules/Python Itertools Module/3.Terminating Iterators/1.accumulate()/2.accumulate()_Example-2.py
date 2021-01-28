from itertools import accumulate
import operator
l1=[1,2,3,4,5]
print(list(accumulate(l1, operator.mul)))
l2=[3,6,2,1,9]
print(list(accumulate(l2, max)))
print(list(accumulate(l2, min)))
# Amortize a 5% loan of 1000 with 4 annual payments of 90
cashflows = [1000, -90, -90, -90, -90]
print(list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt)))