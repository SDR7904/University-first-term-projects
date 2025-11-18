a, b, c = map(int, input().split())

total = a + b + c
if total % 3 != 0:
    result = -1

target = total // 3
at_target = sum([a == target, b == target, c == target])

if at_target == 3:
    result = 0
elif at_target >= 1:
    result = 1
else:
    result = 2

print(result)