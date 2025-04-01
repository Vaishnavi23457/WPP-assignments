class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return Employee(self.name + " & " + other.name, self.salary + other.salary)

    def __sub__(self, other):
        return Employee(self.name, self.salary - other.salary)

    def __str__(self):
        return f"Employee(Name: {self.name}, Salary: {self.salary})"

# Example Usage
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

emp3 = emp1 + emp2
print(emp3)  # Output: Employee(Name: Alice & Bob, Salary: 110000)

emp4 = emp2 - emp1
print(emp4)  # Output: Employee(Name: Bob, Salary: 10000)
