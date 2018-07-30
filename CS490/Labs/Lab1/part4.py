import random as rand
from people import Person


first_names = ["Thomas", "John","Mike","Liz","Joan","Hattie","Emma"]
last_names = ["Smith", "Jones", "Brown", "Miller", "Tran","Cook","Scott"]
python = []
web = []



def random_string(input:list) ->str:
    num = rand.randint(0,len(input)-1)
    return input[num]

def generate_random_students(fname:list,lname:list, number_of_students: int) -> list:
    """creates a list of persons with random names"""
    lst = []
    for _ in range(0,number_of_students):
        lst.append(Person(random_string(fname),random_string(lname)))
    return lst

def random_partion(class1: list, class2: list, students: list):
    """randomly places a student in non one or both class list"""
    for student in students:
        num = rand.randint(0,4)
        if num == 0:
            pass
        elif num == 1:
            class1.append(student)
       
        elif num == 2:
            class2.append(student)

        elif num == 3:
            class1.append(student)
            class2.append(student)
    return

def print_student(students):
    """ prints the students name and its memory location"""
    for student in students:
        print(student.get_full_name() + " "+ str(student))#


student_list = generate_random_students(first_names,last_names,10)

random_partion(python,web,student_list)
# turns all list into a set
python_set = set(python)
web_set = set(web)
student_set = set(student_list)
#finds the students in both classes
common_set = python_set.intersection(web_set)
#finds the student  who have no classes
no_class = student_set.difference(student_set.difference(python_set),web_set)


print()
print("common classes")
print()
print_student(common_set)
print()

print("No class")
print()
print_student(no_class)
print()
