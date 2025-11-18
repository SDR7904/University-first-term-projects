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

prime_list = []

for i in range(1500):
    prime_list.append(is_prime(i))
print(prime_list)