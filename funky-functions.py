def hello():
  foo = 0
  while foo < 3:
    print('counting ' + str(foo))
    foo += 1

def butts(foo):
  print(str(foo))

def plusOne(number):
  return number + 1

hello()
butts(69)
print(str(plusOne(68)))