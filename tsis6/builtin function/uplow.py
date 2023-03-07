s = str(input())
def uplow(a):
    up = 0
    low = 0
    i = 0
    for i in range(len(a)):
        if a[i].isupper():
            up += 1
        if a[i].islower():
            low += 1
        i += 1
    print(up, low)
uplow(s)