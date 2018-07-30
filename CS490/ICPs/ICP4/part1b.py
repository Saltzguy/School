import random as rand
from part1 import *

first_names = ["Thomas", "John","Mike","Liz","Joan","Hattie","Emma"]
last_names = ["Smith", "Jones", "Brown", "Miller", "Tran","Cook","Scott"]
dep =["Production","R&D","Purchasing","H&R","Accounting","Marking"]

def random_family() ->int:
    family = rand.randint(0,10)
    return family

def random_pay() -> int:
    """ returns a random int from 500 -> 1000"""
    pay = rand.randint(500,1000)
    return int(pay)

def random_string(input: list):
    """returns a random item from a list"""
    num = rand.randint(0,len(input)-1)
    return input[num]

def avg_pay(input: list) -> float:
    """Takes a list of employees and finds the avg salary of them"""
    pay = 0
    for emp in input:
        pay += emp.get_salary()
    return pay / len(input)

def call_all_functions(input: list) -> None:
    """takes a list of employees and calls all methods"""
    for emp in input:
        print("{0} {1} {2} {3} {4}".format(emp.get_first_name(), emp.get_last_name(),emp.get_family(), emp.get_salary(), emp.get_department()))


list_of_employee = []
list_of_fulltime = []

# generates a list of employees
for _ in range(10):
   list_of_employee.append(Employee(random_string(first_names),random_string(last_names),random_family(),random_pay(), random_string(dep)))
#generates a list of full time employees
for _ in range(10):
    list_of_fulltime.append(Fulltime_Employee(random_string(first_names),random_string(last_names),random_family(), random_pay(),random_string(dep)))

print()
print("Employee pay")
print(avg_pay(list_of_employee))
print()
print("Fulltime Employee pay")
print(avg_pay(list_of_fulltime))
print()
print("Employee methods")
call_all_functions(list_of_employee)
print()
print("Fulltime Employee methods")
call_all_functions(list_of_fulltime)


#prints the number of employees
print(list_of_employee[0].get_number_of_employee())
p = Employee("j","s",6,500,"dlkasj")
print(p.get_number_of_employee())
del(p)
print(list_of_employee[0].get_number_of_employee())