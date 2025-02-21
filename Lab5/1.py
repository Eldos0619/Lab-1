import re

words=["ac","abb","ba","cb"]

pattern=r'ab*'
for i in words:
    if re.fullmatch(pattern,i):
        print(f'{i} mathes with the pattern')
    else:
        print(f"{i} doesn't matches with the pattern")