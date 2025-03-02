import functools
def multiply_list(numbers):
    return functools.reduce(lambda x,y:x*y,numbers)
numbers=[1,2,3,4]
print(multiply_list(numbers))