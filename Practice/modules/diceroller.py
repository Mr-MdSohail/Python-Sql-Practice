import random
start = input("Welcome to Diceroller !!\nType ""roll"" when youre ready...\n")
if start.lower == 'roll':
    print("You got",random.randint(1,6))
else:
    print("Oops you typed something else, type roll to roll the dice.")

