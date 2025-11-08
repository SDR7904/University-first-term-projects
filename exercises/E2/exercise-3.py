weight, height = input().split()
height = float(height)
weight = float(weight)
if height > 100:
    height /= 100
bmi = weight / (height ** 2)
print(bmi)