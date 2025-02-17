def even_numbers(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield str(i)
            
N = int(input())

gen = even_numbers(N)

print(", ".join(gen))