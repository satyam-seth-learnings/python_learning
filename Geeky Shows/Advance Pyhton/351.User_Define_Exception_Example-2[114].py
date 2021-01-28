class BalanceException(Exception):
    pass
def balancecheck():
    money=10000
    withdraw=9000   #Or withdraw=6000
    balance=money-withdraw
    if (balance<=2000):
        raise BalanceException('Insufficient Balance')
    print(balance)
try:
    balancecheck()
except BalanceException as be:
    print(be)