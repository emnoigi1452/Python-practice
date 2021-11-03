n = int(input())
a = sorted([int(i) for i in input().split(' ')])
sum = 0
for x in range(0, len(a)-1):
    for z in range(x+1, len(a)):
        sum += a[x]*a[z]
else: print(sum)
