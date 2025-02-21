import re

words = ["ab", "cb", "abbb", "abb", "ba"]

pattern = r"ab{2,3}"
for i in words:
    if re.fullmatch(pattern, i):
        print(f"{i} matches with the pattern")
    else:
        print(f"{i} doesn't matches with the pattern")