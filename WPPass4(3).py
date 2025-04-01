n = int(input("enter no of testcases:"))

def panagrams(s):
    s = s.lower()
    for i in range(97, 123):
        if chr(i) not in s:
            return "NOT a Panagram"
    return "YES, its a Panagram"

for i in range(n):
    print(panagrams(input("enter string:")))

