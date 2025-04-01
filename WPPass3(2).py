n=int(input("enter no of testcases:"))

for i in range(1,n+1):
    def isFibo(num):
        a,b=0,1
        while a<num:
            a,b=b,a+b
        if a==num:
            print("isFibo")
        else:
            print("isNotFibo")
for i in range(1,n+1):
    num=isFibo(int(input("enter number:")))


