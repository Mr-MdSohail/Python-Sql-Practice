import os
folder = "myfolder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print("folder created!")
else:
    print("that folder already exists")