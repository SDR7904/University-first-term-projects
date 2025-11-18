def digit_sum(x):
    return sum(int(c) for c in str(x))

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

n = int(input())
b = digit_sum(n)

count = 0
x = n + 1

while True:
    if is_prime(x):
        count += 1
        if count == b:
            print(x)
            break
    x += 1