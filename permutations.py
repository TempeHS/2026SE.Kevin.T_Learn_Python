list = [1, 2, 3]

for x in list:
    for y in list:
        for z in list:
            if x != y and y != z and x != z:
                print(x, y, z)