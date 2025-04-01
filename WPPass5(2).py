n=int(input("enter no of testcases:"))

def  chocolate_bar(num):
    for temp in range(num):
        if num%2!=0:
            temp=(num//2)*(num//2 + 1)   
        else:
            temp=pow(num//2,2)
        return temp
    
for i in range(n):
    num=int(input("enter value:"))
    print(chocolate_bar(num))

            

