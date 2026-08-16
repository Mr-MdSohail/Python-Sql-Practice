# # # 2. Print the multiplication table of a number (entered by user).
a = int(input("Enter number:"))
print(a, "table is :")
for j in range(1,11):
    print(a, "X", j, "=", a*j)