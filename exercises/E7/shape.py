def printer(n,c):
    for i in range(n):
        print(n*c)

n,k,c = input().split()
n = int(n)
k = int(k)

step = (n // k) + 1

for i in range(step):
    printer(n, c)
    n -= k
    if n < 0:
        break