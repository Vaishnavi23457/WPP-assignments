n=int(input("enter no of testcases:"))
def maximizing_xor(L, R):
    max_xor = 0
    for A in range(L, R + 1):
        for B in range(A, R + 1):
            max_xor = max(max_xor, A ^ B)
    return max_xor

if __name__ == "__main__":
    L = int(input())
    R = int(input())
    print(maximizing_xor(L, R))


for i in range(n):
    L = int(input())
    R = int(input())
    print(maximizing_xor(L, R))