a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
total = a + b + c
if total == 180 and a != 0 and b != 0 and c != 0:
    print("Yes")
else:
    print("No")