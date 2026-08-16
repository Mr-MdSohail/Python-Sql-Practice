import random
characters = "abcdefghijklmnopqrstuvxyz1234567890!@#$%^&*()"
length=int(input("Enter length of password: "))
password_list = random.choices(characters, k=length)
print("".join(password_list))