# 2. Write a program that keeps asking the user to enter a password until they enter the correct one.
a = input("Enter password: ")
while(a!="sohail"):
    print("Password incorrect. Try again.")
    a=input("Enter password: ")
print("Correct password")