len = int(input()); sum = 0
a = [int(x) for x in input().split(' ')]
b = [int(z) for z in input().split(' ')]
for i in range(0, len): sum += (a[i] ** b[i]) % 100000000
print(sum)
