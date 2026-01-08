n = int(input())
result = []
for i in range(n):
    t = int(input())
    inp = input()
    a,b = map(set, inp.split())
    # if a == b and len(inp) == 2*t + 1:
    if a == b and len(a) == len(b):
        result.append("YES")
    else:
        result.append("NO")
for i in result:
    print(i)