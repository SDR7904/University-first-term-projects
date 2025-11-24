n = int(input())
max_cost, name = 0, ""
while n > 0:
    a,b = input().split()
    if int(b) > max_cost:
        name = a
        max_cost = int(b)
    n -= 1
print(name)