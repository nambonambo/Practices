#1 example 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
#2 example

for x in "banana":
  print(x)
  
#3 example 

for x in range(6):
  print(x)
  
#4example

for x in range(2, 6):
  print(x)
  
#5 example

for x in range(2, 30, 3):
  print(x)
  
#6 example 

for x in range(6):
  print(x)
else:
  print("Finally finished!")
  
#7 example 

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
#8 example 

for x in [0, 1, 2]:
  pass