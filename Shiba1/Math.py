inp = [int(i) for i in input().split(' ')]
n,m = inp[0],inp[1]
sqr = lambda i: i*i
res = int(((sqr(n)*sqr(n+1)) / 4) % m)
print(res)
