a = 0
b = 1
list = [0,1]
for i in range(18):
  c=a+b
  list.append(c)
  a = b
  b = c
print("The first twenty Fibonacci Numbers are: ",list)
