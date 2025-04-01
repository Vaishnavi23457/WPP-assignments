n=int(input("enter no of testcases:"))


def square_integers(a,b):
    count=0
    for i in range(a,b+1):
        if (int(i**0.5))**2==i:
            count+=1
    return count

for i in range(n):
    print(square_integers(int(input("enter lower limit:")),int(input("enter upper limit:"))))
