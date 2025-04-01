n = int(input("enter no of testcases:"))
for i in range(1,n+1):
    def heightofTree(cycles):
        height=1
        for i in range(1,cycles+1):
            if i%2==0:
                height+=1
            else:
                height*=2
        return height

for i in range(1,n+1):
    cycles=heightofTree(int(input("enter number:")))
    print(cycles)