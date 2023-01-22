# Exercicio Indexação
x = 1
y = 2

if x > y:
  x = y
  z = x-1
  if x < z:
    x=y+1
    print (z)
  print (x)  
else:
  y = x
  x = y-1
  print(y)