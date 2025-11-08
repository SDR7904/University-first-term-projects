result = ""
for i in range(3):
    inp = input("")
    if len(inp) == 1:
        inp = "0" + inp
    result += inp
    if i < 2:
        result += " : "
print(result)