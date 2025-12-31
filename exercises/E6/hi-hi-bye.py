n = int(input())
guys = list(input().split())

# say hi loop
for i in range(1, n):
        for j in range(i-1,-1,-1):
            print(f"{guys[i]}: salam {guys[j]}!")
# say bye loop
for i in range(n):
    print(f"{guys[i]}: khodafez bacheha!")
    for j in range(i+1,n):
        print(f"{guys[j]}: khodafez {guys[i]}!")
