import random
def starrySky(density, width, height):
  count = 0
  for k in range(0, height):
    for j in range(0, width):
      r = random.randint(1, 100)
      if r <= density * 100:
        print("*", end=" ")
        count += 1
      else:
        print(" ", end=" ")
      pass
    print(" ")
  print("Amount of stars: " + str(count))
