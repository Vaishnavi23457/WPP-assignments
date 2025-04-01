class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert(head,newnode):
    if head is None:
        return newnode
    else:
        tem=head
        while tem.next is not None:
            tem=tem.next
        tem.next=newnode
        return head
def delete(head):
    tem=head
    while tem.next is not None:
        tem2=tem
        tem=tem.next
    tem2.next =None
    return head
def show(head):
    tem=head
    while tem is not None:
        print(tem.data,end="->")
        tem=tem.next
num=int(input("enter your linklist size: "))
head=None
for i in range(num):
    newnode=node(int(input("enter your new data ")))
    head=insert(head,newnode)
show(head)
k=1
while k is not 0:
    k=int(input("\n1:insert element\n2:delete element\n0:exit the program  :"))
    if k==1:
        newnode=node(int(input("enter your new data ")))
        head=insert(head,newnode)
    elif k==2:
        head=delete(head)
    elif k==0:
        k=0
    else:
        print("you are enter wronng data")
show(head)