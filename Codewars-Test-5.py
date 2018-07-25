def solve_puzzle (clues):


    return ( clues )

print(solve_puzzle(( 2, 2, 1, 3,
                     2, 2, 3, 1,
                     1, 2, 2, 3,
                     3, 2, 1, 3 )))
xnum = 0
for x1 in range(1,5):
    for x2 in range(1, 5):
        for x3 in range(1, 5):
            for x4 in range(1, 5):
                if (x1 != x2) and (x1 != x3) and (x1 != x4) and (x2 != x1) and (x2 != x3) and (x2 != x4) and (x3 != x1) and (x3 != x2) and (x3 != x4) and (x4 != x1) and (x4 != x2) and (x4 != x3):
                    xnum += 1
                    print(str(xnum) + ' ' + str(x1) + ' ' + str(x2) + ' ' + str(x3) + ' ' + str(x4))
