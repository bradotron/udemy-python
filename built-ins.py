import random

randInt = 0
tries = 0
while randInt != 69:
  randInt = random.randint(0, 100)
  tries += 1
  print(randInt)
if tries != 69:
  print('nice try ' + str(tries))
else:
  print('super nice ' + str(tries))
