def divisible_by_3_and_4(N):
    for i in range(N + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
N = int(input())

gen = divisible_by_3_and_4(N)

print(", ".join(str(num) for num in gen))