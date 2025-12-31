n, m = map(int, input().split())
bless_status = [0 for _ in range(n)]
result = ""
for i in range(m):
    # periods.append(input())
    period = input()
    for j in range(n):
        if period[j] == "W":
            bless_status[j] += 1
for i in range(n):
    if bless_status[i] % 2 == 0:
        result += "B"
    else:
        result += "F"
print(result)