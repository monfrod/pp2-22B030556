filename = "path/to/your/textfile.txt"

with open(filename, "r") as file:
    count = 0
    for line in file:
        count += 1

print("Number of lines in the file:", count)
