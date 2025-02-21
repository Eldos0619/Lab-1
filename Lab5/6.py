import re

chars = ["Hello, world", "a b", "Python", "ACB", ",Test."]

pattern = r"[ ,.]"

replacement = ":"

for i in chars:
    new_string = re.sub(pattern, replacement, i)
    print(f"Before: {i} | After: {new_string}")