a = input()
b = input()
c = input()
n = len(a)//5
letters = {
    'T': ["*****", "oo*oo", "oo*oo"],
    'A': ["oo*oo", "o***o", "*ooo*"],
    'X': ["*ooo*", "oo*oo", "*ooo*"],
    'M': ["**o**", "*o*o*", "*ooo*"],
    'N': ["*ooo*", "*o*o*", "*ooo*"]
}
result = ""
for i in range(1,n+1):
    letter = [a[5*(i-1):5*i],b[5*(i-1):5*i],c[5*(i-1):5*i]]
    # chars.append([a[5*(i-1):5*i],b[5*(i-1):5*i],c[5*(i-1):5*i]])
    for key, value in letters.items():
        if letter == value:
            result += key
            break

print(result)