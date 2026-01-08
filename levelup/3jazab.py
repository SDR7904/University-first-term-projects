t = int(input())
result = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    # a = set(map(int, input().split()))
    r = -1
    for j in range(n):
        if a[j] == a[j+1] and a[j+1] == a[j+2]:
            r = a[j]
            # result.append(r)
    # if r == -1:
    result.append(r)
for i in result:
    print(result)
