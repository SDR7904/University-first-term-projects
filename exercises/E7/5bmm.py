def counter(n):
    r = n
    result = set([1])
    i = 2
    while i <= n:
        if r % i == 0:
            result.add(i)
            r //= i
        else:
            i += 1
    if len(result) >= 2 and not n in result:
        result.add(n)
    return result

numbers = list(map(int, input().split()))
counts = [set(counter(numbers[i])) for i in range(5)]

bmm = counts[0].intersection(counts[1])
for i in range(1, 4):
    bmm = bmm.intersection(counts[i+1])

print(max(bmm))