import math
prime = lambda num: [num % i == 0 for i in range(2, int(math.sqrt(num))+1)].count(True) == 0 and num >= 2
# do like some inputs later on to test it idk
