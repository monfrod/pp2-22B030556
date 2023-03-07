def check_palindrome(string):
    string = string.replace(" ", "").lower()
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True
a = str(input())
print(check_palindrome(a))