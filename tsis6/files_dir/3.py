import os
path = str(input("Path: "))
if os.path.exists(path):
    print(f"{path} exists")
else:
    print(f"{path} does not exist")