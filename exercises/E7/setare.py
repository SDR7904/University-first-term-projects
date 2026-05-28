def triangle(n):
    for i in range(n,0,-1):
        print(i*"*")
def square(n):
    for i in range(n):
        print(n*"*")

n, shape = input().split()

if(shape == "t"):
    triangle(int(n))
elif(shape == "s"):
    square(int(n))