import random
import time
guess_num = random.randint(1,10)
user_num = 0
while user_num != guess_num:
    user_num = int(input("Enter number: "))
    if user_num != guess_num:
        time.sleep(0.5)
        print("Wrong guess. Try again.")
print("Checking your guess...")
time.sleep(1.5)
print("You've guessed it correct!!")
    