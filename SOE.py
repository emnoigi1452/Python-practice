import numpy as np

limit = int(input("Calculate primes until: "))
k = np.full(limit+1, True)

k[0] = False
k[1] = False

for n in range(0, limit+1):
	if k[n]:
		for o in range(2, int(limit/n)+1):
			k[o*n] = False
	else:
		continue

for j in range(0, limit+1):
	if k[j]:
		print(str(j), end=" ")
	else:
		continue
