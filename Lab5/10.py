import re

strings = ["helloWorld", "aBC", "pythonBest", "testProgramm"]

pattern = r"(?=[A-Z])"

replacement = "_"

for string in strings:
    new_string = re.sub(pattern, replacement, string)
    new_string =  new_string.lower()
    print(f"Before: {string} | After: {new_string}")