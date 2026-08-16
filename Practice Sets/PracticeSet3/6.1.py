# write a program that counts how many vowels are in a given string.
sentence = str(input("enter sentence: "))
vowels = ['a','e','i','o','u']
sum = 0

for char in sentence:
    if char in vowels:
        sum += 1
print(f"There are {sum} vowels in this sentence.")