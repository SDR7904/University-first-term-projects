n = int(input())
guys = list(input().split())

# say hi loop
for i in range(n):
    if i > 0:
        for j in range(i):
            print(f"{guys[i]}: salam {guys[j]}!")
# say bye loop
for i in range(n):
    print(f"{guys[i]}: khodafez bacheha!")
    for j in range(i+1,n):
        print(f"{guys[j]}: khodafez {guys[i]}!")
