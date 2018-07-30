


class Employee(object):

    #counts the number of employee
    number_of_employee = 0
    
    #constructer
    def __init__(self, fname: str, lname: str, family: int, salary: int, department: str):
        
        if type(fname) == str and type(lname) == str and type(family) ==int and type(salary) == int and type(department) == str:
            #privite atribues and methods
            self.__increment_employee_count__()
            self.__fname = fname
            self.__lname = lname
            self.__family = family # family count is only for tax purposes
            self.__salary = salary
            self.__department = department
        else:
            raise TypeError
            
    #decerments the number of employees
    def __del__(self):
        self.__class__.number_of_employee -= 1
    # employee count + 1
    def __increment_employee_count__(self):
         self.__class__.number_of_employee += 1
    #returns the employee salary 
    def get_salary(self) -> int:
        return self.__salary
    #returns the first name
    def get_first_name(self) -> str:
        return self.__fname
    #returns the last name
    def get_last_name(self) -> str:
        return self.__lname
    #returns the number of family
    def get_family(self) ->int:
        return self.__family
    #returns the department
    def get_department(self) -> str:
        return self.__department
    #returns the number of employees
    def get_number_of_employee(self) -> int:
        return self.__class__.number_of_employee
    
    def set_family(self, family: int) -> None:
        self.__family = family




class Fulltime_Employee(Employee):
    
    #uses the same __init__ as Employee class

    #counts the number of full time employees
    number_of_employee = 0

    #increses the number of full time employees
    def __increment_employee_count__(self):
        self.__class__.number_of_employee += 1
      
    #decerment the number of employees
    def __del__(self):
        self.__class__.number_of_employee -= 1

