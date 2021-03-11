import csv
import os

#


class Calculator:
    def summ(self, a, b):
        return a+b

    def conc(self, a, b):
        return a-b

    def dev(self, a, b):
        return a/b

    def mult(self, a, b):
        return a*b


a = Calculator()

print("class Calculator:\n")

print(a.summ(5, 4))
print(a.conc(5, 4))
print(a.dev(6, 2))
print(a.mult(5, 4))

print("--=--=--=--=--")
#


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2*(self.width + self.length)

    def print_info(self):
        print('Rectangle Info\n')
        print('Width: ', self.width)
        print('Length: ', self.length)
        print('Area: ', self.area())
        print('Perimeter: ', self.perimeter())


r = Rectangle(5, 10)

r.print_info()

print("--=--=--=--=--")
#


class Employee:

    r = []

    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def readFile(self, filename):
        with open(os.path.dirname(__file__)+'/'+filename, 'r') as file:
            reader = csv.DictReader(file)
            if len(self.r) == 0:
                for row in reader:
                    self.r += [dict(row)]

    def getLowestSalary(self):
        self.readFile('dataset1.csv')
        salaries = [row['salary'] for row in self.r]
        print("Lowest salary employee(s):\n")
        lowest = [row for row in self.r if row['salary'] == min(salaries)]
        for employee in lowest:
            print('=--=--=--=')
            print('Name: ', employee['name'])
            print('Surname: ', employee['surname'])
            print('Age: ', employee['age'])
            print('Salary: ', employee['salary'])
            print('=--=--=--=')

    def getOldestEmployee(self):
        self.readFile('dataset1.csv')
        salaries = [row['age'] for row in self.r]
        print("Oldest employee(s):\n")
        oldest = [row for row in self.r if row['age'] == max(salaries)]
        for employee in oldest:
            print('=--=--=--=')
            print('Name: ', employee['name'])
            print('Surname: ', employee['surname'])
            print('Age: ', employee['age'])
            print('Salary: ', employee['salary'])
            print('=--=--=--=')


e = Employee('Luka', 'Urushadze', '19', '2000')

e.getLowestSalary()
e.getOldestEmployee()
