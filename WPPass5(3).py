n=int(input("enter no of testcases:"))
def Bigger_is_Greater(s):
    s=list(s)
    i=len(s)-1
    while i>0 and s[i-1]>=s[i]:
        i-=1
    if i<=0:
        return "no answer"
    j=len(s)-1
    while s[j]<=s[i-1]:
        j-=1
    s[i-1],s[j]=s[j],s[i-1]
    s[i:]=s[len(s)-1:i-1:-1]
    return "".join(s)

for i in range(n):
    s=input("enter string:")
    print(Bigger_is_Greater(s))
