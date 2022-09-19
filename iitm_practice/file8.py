x = int(input())
y = int(input())
z = int(input())

# Block-1 Start
if x > 0 or y > 0 or z > 0:
    if (x > 0 and y > 0) or (y > 0 and z > 0) or (z > 0 and x > 0):
        if x > 0 and y > 0 and z > 0:
            print('P3')
        else:
            print('P2')
    else:
        print('P1')
# Block-1 End

# Block-2 Start
if x < 0 or y < 0 or z < 0:
    if (x < 0 and y < 0) or (y < 0 and z < 0) or (z < 0 and x < 0):
        if x < 0 and y < 0 and z < 0:
            print('N3')
        else:
            print('N2')
    else:
        print('N1')
# Block-2 End