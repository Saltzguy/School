
import random



def main():
    rand_num = random.randint(0,9)# generates a random number between 0 and 9
    guess_num = -1
    while(guess_num != rand_num):
        guess_num = int(input("What is your guess -> "))
        if guess_num < rand_num:  
            print("Your guess was low")
        elif guess_num > rand_num:
            print("your guess was high")
        else:
            print("you got it!")
main()
