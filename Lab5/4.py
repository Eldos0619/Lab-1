import re

strings = ["Hello_world!", "abc", "Python", "money","Test"]

pattern = r"^[A-Z][a-z]+$"

for string in strings:
    if re.fullmatch(pattern, string):
        print(f"{string} matches with the pattern")
    else:
        print(f"{string} doesn't matches with the pattern")