with open('A.txt', 'r') as file1, open('B.txt', 'w') as file2:
    file2.write(file1.read())
