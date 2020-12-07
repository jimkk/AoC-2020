import numpy

with open("input.txt", "r") as f:
    data = f.readlines()
# data2 = data.copy()


slopes = [[1,1], [1,3], [1,5], [1,7], [2,1]]
total = 1
for slope in slopes:
    treecount = 0
    loc = numpy.array([0,0])
    while loc[0] < len(data)-1:
        loc += slope
        if loc[1] >= len(data[0])-1:
            loc[1] = loc[1] - len(data[0]) + 1
        if data[loc[0]][loc[1]] == '#':
            treecount += 1
    print(treecount)
    total *= treecount
print(total)
