#1 example

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#2 example 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
#3 example

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")