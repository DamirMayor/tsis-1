#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#3
for x in range(6):
  print(x)


#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#Examples
for x in "banana":
  print(x) 
for x in range(2, 6):
  print(x)
for x in range(2, 30, 3):
  print(x) 
for x in range(6):
  print(x)
else:
  print("Finally finished!")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
for x in [0, 1, 2]:
  pass
