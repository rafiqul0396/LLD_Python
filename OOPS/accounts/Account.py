class Accounts:
    def __init__(self,id,name,balance):
        self.id = id
        self.name=name
        self.balance=balance

    def  deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount


    def transfer(self,other,amount):
        self.withdraw(amount)
        other.deposit(amount)


if __name__=='__main__':
    Alice=Accounts(1,'alice',500)
    Bob=Accounts(2,'Bob',1000)
    Alice.transfer(Bob,500)
    print(Alice.balance)
    print(Bob.balance)
