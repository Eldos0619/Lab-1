import re

words=["hello", "a_b", "Python", "ACB", "alj!@#$%^&*KHL*b"]

pattern=r'^a.*b$'

for i in words:
    if re.fullmatch(pattern,i):
        print(f'{i} mathes with the pattern')
    else:
        print(f"{i} doesn't matches with the pattern")