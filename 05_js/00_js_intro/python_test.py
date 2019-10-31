def ssafy(x):
  return x + 1


print(list(map(ssafy, [1, 2, 3])))

print(list(map(lambda x: x + 1, [1, 2, 3])))
