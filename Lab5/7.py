import re

strings = ["hello_world!", "aBc", "Python_programm", "abc_bca", "test"]


for string in strings:
    new_strings = re.split("_", string)
    new_string = ""
    for i in new_strings:
        new_string += i.capitalize()
        
        
    
    print(f"Before: {string} | After: {new_string}")