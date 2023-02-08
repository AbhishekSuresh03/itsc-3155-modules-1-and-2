def shift_lower_case(string):
    lower_case = ""
    upper_case = ""
    for char in string:
        if char.islower():
            lower_case += char
        elif char.isupper():
            upper_case += char
    return lower_case + upper_case

input_string = input("Enter a string: ")
print("Output string:", shift_lower_case(input_string))
