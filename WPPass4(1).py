n=int(input("enter no of testcases:"))

def minMoves_to_palindrome(s):
    count = 0
    length = len(s)
    s = list(s)
    for i in range(length // 2):
        while s[i] != s[length - i - 1]:
            if s[i] < s[length - i - 1]:
                s[length - i - 1] = chr(ord(s[length - i - 1]) - 1)
            else:
                s[i] = chr(ord(s[i]) - 1)
            count += 1
    return count 

for i in range(n):
    print(minMoves_to_palindrome(input("enter your string:")))

