import re

strings = ["Hello,World", "aBc", "Python", "ACB", "TesT"]

pattern = r"(?=[A-Z])"

for string in strings:
    new_string = list(filter(None, re.split(pattern, string)))  
    print(f"Before: {string} | After: {new_string}")