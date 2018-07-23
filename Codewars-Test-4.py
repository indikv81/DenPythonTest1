def find_it(seq):
    scount = list(filter(lambda x: seq.count(x) % 2 != 0, seq))
    return scount[0]


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))