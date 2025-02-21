import re

words = ["a_b", "f-c", "A-C", "hello_world"]

pattern = r"^[a-z]+_[a-z]+$"

for i in words:
    if re.fullmatch(pattern, i):
        print(f"{i} matches with the pattern")
    else:
        print(f"{i} doesn't matches with the pattern")