r,c = input().split()
c = int(c)
r = int(r)
if c <= 10:
    direction = "Right"
    cgo = c
else:
    direction = "Left"
    cgo = 21 - c
rgo = 11 - r
print(direction, rgo, cgo)