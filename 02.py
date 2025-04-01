class queue:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert(rare,newqueue):
    if  rare is None:
        return newqueue
    else:
        rare.next=newqueue
        rare=rare.next
        return  rare
def delete(front):
    front=front.next
    return front
def show( rare,front):
    tem=front
    while tem is not None:
        print(tem.data,end="->")
        tem=tem.next
num=int(input("enter your QUEUE size"))
rare=None
front=None
for i in range(num):
    newqueue=queue(int(input("enter your new data")))
    if front==None:
        front=newqueue
    rare=insert( rare,newqueue)
show( rare,front)
k=1
while k is not 0:
    k=int(input("\nEnter your choice  1:insert element\n2:delete element\n0:exit the program/t"))
    if k==1:
        newqueue=queue(int(input("enter your new data")))
        rare=insert( rare,newqueue)
    elif k==2:
        front=delete( front)
    elif k==0:
        k=0
    else:
        print("you are enter wronng data")
show( rare,front)
