class bank:
    def  __init__(self,account):
        self.total=0
        self.account=account
        self.transaction=[]
    def tran(self,transaction):
        if transaction>0:
            self.transaction.append(f"deposit={transaction}")
            self.total+=transaction
        elif transaction<0:
            self.transaction.append(f"credit={-transaction}")
            self.total+=transaction
    def show(self):
        print(f"account no.:{self.account}")
        print(self.transaction)
        print(f"total amount in bank :{self.total}")
acc=int(input("enter account number  "))
info=bank(acc)
k=1
while k is not 0:
    amount=int(input("enter you amount if deposit :use postive number\ncredit : use negative value  "))
    info.tran(amount)
    k=int(input("if you want more transaction :1,exit the transaction:0  "))
info.show()


