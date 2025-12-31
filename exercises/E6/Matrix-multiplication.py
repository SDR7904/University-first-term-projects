a,b,c = map(int, input().split())
# ma = [a*[]]
# mb = [b*[]]
ma, mb = [], []
# row = c*[0]

# mf = [a * row]
# no_err = True

for i in range(a):
    ma.append(list(map(int, input().split())))
    # if len(ma[i]) != b:
    #     no_err = False
    #     print("declined.")
    #     break
for j in range(b):
    mb.append(list(map(int, input().split())))
    # if len(ma[i]) != b:
    #     no_err = False
    #     print("declined.")
    #     break

# print(ma)
# print(mb)
# print(mf)
mf = []
for i in range(a):
    mf.append([])
    for k in range(c):
        s = 0
        for j in range(b):
            s += ma[i][j] * mb[j][k]
            # if j == b-1:
        mf[i].append(s)
        # mf[i][k] = s
# print(mf)
for i in range(a):
    for j in range(c):
        print(mf[i][j], end=" ")
    if i < a-1:
        print()