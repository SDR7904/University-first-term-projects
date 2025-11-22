Origin = int(input())
Destination = int(input())
positions = [[1,4], [2,3]]
if Origin == Destination:
    print(0)
else:
    for i in range(2):
        if Origin in positions[i]:
            if Destination in positions[i]:
                print(2)
                break
            else:
                print(1)
                break
        # if [Origin, Destination] == positions[i] or [Destination, Origin] == positions[i]:
        #     print(2)
        #     break
        # else:
        #     print(1)
        #     break