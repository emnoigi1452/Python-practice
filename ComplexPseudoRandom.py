import random
import math

def complex_rand(n):
    n = min(max(n, 0), 17)
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    b_rand = lambda: random.randint(1, (2 ** 64))
    p_rand = lambda: primes[random.randint(0,17)]
    med = 1
    for i in range(n):
        med = int(math.sqrt(med * b_rand())) ^ p_rand()
    d = [int(c) for c in str(med)]
    for x in range(len(d)):
        d[x] = (d[x] << p_rand()) ^ ((p_rand() ** n) & b_rand())
    med = p_rand()
    for e in d:
        ef = float(e) / float(10 ** len(str(e)))
        med = int(math.sqrt(med * e * int(b_rand() * ef))) ^ len(d)
    return (med << (n+3)) % ((p_rand() ** 64) % (2 ** 128))