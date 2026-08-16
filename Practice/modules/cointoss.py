import random
coinsides = ["Head", "Tail"]
start = input("Welcome to CoinToss !!\nType ""toss"" when youre ready...\n")
if start.lower() == 'toss':
    print("You got",random.choice(coinsides))
else:
    print("Oops you typed something else, type toss to toss the coin.")