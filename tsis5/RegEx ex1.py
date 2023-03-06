import re
pattern = r'a[b]*'
str = str(input())
match = re.match(pattern, str)
print(match)