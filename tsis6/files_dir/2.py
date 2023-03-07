import os

path = '/Users/yunus/Documents/GitHub/pp2-22B030556/tsis1/example 1.py'

if os.path.exists(path):
    print(f"{path} exists")
else:
    print(f"{path} does not exist")

if os.access(path, os.R_OK):
    print(f"{path} is readable")
else:
    print(f"{path} is not readable")

if os.access(path, os.W_OK):
    print(f"{path} is writable")
else:
    print(f"{path} is not writable")

if os.access(path, os.X_OK):
    print(f"{path} is executable")
else:
    print(f"{path} is not executable")
