
student_names = []
num_students = int(input("enter no of students: "))

for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    #name does not exceed 15 characters
    if len(name) > 15:
        name = name[:15]
    student_names.append(name)

# Reverse the names and display them
reversed_names = [name[::-1] for name in student_names]

print("Reversed names of the students:")
for name in reversed_names:
    print(name)