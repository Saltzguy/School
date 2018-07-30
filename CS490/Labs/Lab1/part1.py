"""
John Widner
06-13-18
Lab 1
"""
import re  # used to search passwords

# Prompt User for username
username = str(input("Choose your username: "))
# Prompt User for password
password = str(input("Choose your password: "))
password_pass = 0
# While loop will only exit when all requirements have been met
while password_pass != 6:
    # Test Min Length
    if len(password) >= 6:
        password_pass += 1
    else:
        print("Error 1: The password you have chosen is too short. Try Again.")
        password_pass = 0
        password = str(input("Choose new password: "))
        continue

    # Test Max Length
    if len(password) <= 16:
        password_pass += 1
    else:
        print("Error 2: The password you have chosen is too long. Try Again.")
        password_pass = 0
        password = str(input("Choose a new password: "))
        continue

    # Test Special Character Present
    if re.search('[!@#$%&]', password):
        password_pass += 1
    else:
        print("Error 3: The password must have a spec char. Try Again.")
        password_pass = 0
        password = str(input("Choose a new password: "))
        continue
    # Test Capital Letter Present
    if re.search('[A-Z]', password):
        password_pass += 1
    else:
        print("Error 4: The password must have at least one capital letter")
        password_pass = 0
        password = input("Choose a new password: ")
        continue
    # Test Lowercase Letter Present
    if re.search('[a-z]', password):
        password_pass += 1
    else:
        print("Error 5: The password must have at least one lowercase letter")
        password_pass = 0
        password = input("Choose a new password: ")
        continue
    if re.search('[0-9]',password):
        password_pass += 1
    else:
        print("Error 6: The password must have at least one number")
        password_pass = 0
        password = input("Choose a new password: ")
        continue

print("Thank You. Your username and password has been saved.")
exit()
