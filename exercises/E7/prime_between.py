def is_prime(n):
    if(n == 1):
        return 0
    elif(n > 3):
        for i in range(2, (n//2)+1):
            if n%i == 0:
                return 0
    return 1

a = int(input())
b = int(input())

prime_list = []

for j in range(a,b+1):
    if(is_prime(j)):
        print(j)