x, y = [], []
for i in range(3):
    x_i,y_i = input().split()
    x_i = int(x_i)
    y_i = int(y_i)
    if x_i not in x:
        x.append(x_i)
    else:
        x.remove(x_i)
    if y_i not in y:
        y.append(y_i)
    else:
        y.remove(y_i)
print(x[0], y[0])