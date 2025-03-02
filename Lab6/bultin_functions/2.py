def count_letters(str):
    uppersum=0
    lowersum=0
    for i in str:
        if i.isupper():
            uppersum+=1
        else:
            lowersum+=1
    return f'UpperLetters:{uppersum},LowerLetters:{lowersum}'
str="AssGhJki"
print(count_letters(str))

