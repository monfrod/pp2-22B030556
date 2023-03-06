def snake_to_camel(s):
    return ''.join(word.title() for word in s.split('_'))


string = input("Enter a snake case string: ")
camel_string = snake_to_camel(string)

print("Camel case string: ", camel_string)