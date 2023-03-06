import re

string = input("Enter a string: ")
new_string = re.sub(r"([A-Z])", r" \1", string).strip()

print("Original string: ", string)
print("New string: ", new_string)