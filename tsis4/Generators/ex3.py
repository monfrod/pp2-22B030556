n = int(input())
divBy34 = [i for i in range(0, n) if (i%3 == 0 or i%4 == 0)]
print(divBy34)

def divChecker(n):
    for i in range(n):
        if i%3 == 0 or i%4 == 0:
            value = True
        else:
            value = False
        print(i, value)

divChecker(n)