ls1 = [2,5,7]
ls2 = [1,6,3]
ls3 = [0,1,2]
ls4 = [-1,-2,-3]
ls5 = [0,0,0]
x = 0
for count in ls3:
    ls3[count] = ls1[-1] + ls2[-1]
    ls1.pop(-1)
    ls2.pop(-1)
for invert in ls4:
    ls5[invert]= ls3[x]
    x += 1
print(ls5)
