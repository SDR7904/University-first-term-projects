sufferers_shekarestan = int(input())
deceased_shekarestan = int(input())
sufferers_namakestan = int(input())
deceased_namakestan = int(input())
shekarestan = sufferers_shekarestan - deceased_shekarestan
namakeestan = sufferers_namakestan - deceased_namakestan
if namakeestan > shekarestan:
    print("Namakestan")
elif namakeestan == shekarestan:
    print("Equal")
else:
    print("Shekarestan")