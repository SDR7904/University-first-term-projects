l, r, x, y = map(int, input().split())
result = max(0, min(r, y) - max(l, x) + 1)
print(result)