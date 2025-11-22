a, b, c, d, e, f,  = map(int, input().split())
ice = [d, e, f]
ice.remove(max(ice))
if (a >= ice[0] and b >= ice[1]) or (a >= ice[1] and b >= ice[0]):
    print("zende mimuni")
else:
    print("dari mimiri")