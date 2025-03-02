def palindrom(str):
    if str==str[::-1]:
        print ("It is palindrom")
    else:
        print ("It is not palindrom")
str=input("str:")
print(palindrom(str))