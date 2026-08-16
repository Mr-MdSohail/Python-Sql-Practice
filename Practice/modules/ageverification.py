from datetime import datetime
print("⚠️  Age verification needed to access this website  ⚠️")
user_year = int(input("Enter your birth year: "))
today_year = datetime.now().year
while user_year<today_year-100 or user_year>today_year:
    print("Please enter valid year.")
    user_year = int(input("Enter your birth year: "))
if ((today_year)-(user_year)>=18):
    print("Age verification complete , you can access the website.")
else:
    print("Sorry! You are not allowed to access the website.")

