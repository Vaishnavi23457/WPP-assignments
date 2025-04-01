import random

#generate 100 random integers that are either 0 or 1
random_integers = [random.randint(0, 1) for _ in range(100)]

#find the longest run of zeroes
max_run = 0
current_run = 0

for num in random_integers:
    if num == 0:
        current_run += 1
        if current_run > max_run:
            max_run = current_run
    else:
        current_run = 0

print("Random integers:", random_integers)
print("Longest run of zeroes:", max_run)