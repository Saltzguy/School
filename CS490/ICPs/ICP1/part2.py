def reverse_name():
    # takes in two strings inputs and returns the strings to geter
    fname = input("What is your first name -> ") 
    lname = input("what is your last name -> ")
    name = fname + " " + lname
    print(name[::-1])

reverse_name() # prints the user name in reverse

def quot_rem(num1, num2):
    quot = num1 // num2
    rem = num1 % num2
    print("Quotient is " + str(quot) + " and remainder is " + str(rem))


def get_number():
    #gets two numbers and 
    num1 = -1
    num2 = -1
    while(num1 < -1 or num2 <= 0):
        num1 = int(input("What is the first number ->"))
        num2 = int(input("What is the second number ->"))
    if num1 < -1:
        print("The first number needs to be greater than -1") #
    if num2 <= 0:
        print("The second number needs to be greater than 0")
    quot_rem(num1, num2)

get_number()
