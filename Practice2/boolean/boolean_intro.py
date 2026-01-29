#1 example 

print(bool("Hello"))
print(bool(15))

#2 example 

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#3 example

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#4 example

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#5 example 

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#6 example

def myFunction() :
  return True

print(myFunction())