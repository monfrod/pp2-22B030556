import re
s = "asdvasdvasdvasdvasdvasd"
result = re.split("asd", s, maxsplit = 6)
print (result)