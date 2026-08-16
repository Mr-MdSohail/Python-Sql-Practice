# 1. Write a program that asks the user for a number and prints whether it is 
# positive, negative, or zero.
a = int(input("Enter number: "))
if(a>0):
    print("Its a positive number")
elif(a==0):
    print("You entered 0")
elif(a<0):
    print("Its a negative number")