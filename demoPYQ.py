list1 =["jack", "robin", "dick", "hood"]
for name in list1:
    if "bin" in name:
        break

    print (((name*3)[::-2]).replace('d', '$'))


def test (str):
    str2=""
    for i in range(len(str)-1,-1,-1):
        str2=str2+str[i]
    print(str2)

test ("web programming")


str="Wednesday"
d={
"Hello": str.isdigit()
}
for i in str:
    d[i] == str.count('d')
print (d)