import math
n=int(input("Number of sided:"))
l=int(input("Length of side:"))
p=n*l
a=l/2*math.tanh(180/n)
print(f'Area:{p*a/2}')