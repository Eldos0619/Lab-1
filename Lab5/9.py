import re

strings = ["HelloWorld", "aBc", "Python", "ACB", "TeSt"]

pattern = r"(?=[A-Z])"

replacement = " "

for string in strings:
    new_string = re.sub(pattern,replacement, string)
    print(f"Before: {string} | After: {new_string}")