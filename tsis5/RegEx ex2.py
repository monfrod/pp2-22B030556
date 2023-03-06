import re

string = input("Enter a string: ")
pattern = r"a(bb|bbb)"

if re.match(pattern, string):
    print("Match found!")
else:
    print("Match not found.")
