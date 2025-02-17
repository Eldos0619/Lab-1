def sqaure_of_numbers(N):
    for num in range(N + 1):
        yield num**2

N = int(input())
gen = sqaure_of_numbers(N)

for i in gen:
    print(i)