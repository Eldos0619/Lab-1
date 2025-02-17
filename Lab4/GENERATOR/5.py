def to_zero(N):
    for i in range(N, -1, -1):
        yield i
N = int(input())
gen = to_zero(N)

print(", ".join(str(num)for num in gen))       