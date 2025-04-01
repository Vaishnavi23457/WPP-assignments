
n=int(input("enter no of testcases:"))

def find_dividing_digits(num):
    count = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        temp = temp // 10
        if digit != 0 and num % digit == 0:
            count += 1
    return count

for i in range(1, n+1):
    num = int(input("enter your number:"))
    result = find_dividing_digits(num)
    print(f"Number of digits in {num} that divide {num} is: {result}")