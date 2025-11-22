persons = [[],[],[]]
result = 0
for i in range(3):
    for j in range(2):
        a = int(input())
        persons[i].append(a)
        if j == 1:
            minimum = min(persons[i])
            result += minimum
print(result)