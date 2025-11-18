n, k = map(int, input().split())
a = map(int, input().split())

print(sum(x // k for x in a))