#Exercicio Indexação
x = int(input("Escolha um número para X: ")) 
y = int(input("Escolha um número para Y: "))

if x > y: 
    y = x 
    y=x-1 
if x < y: 
    x=y+1 
    print (y) 
    print (x)
else: 
    y = x 
    x = y-1 
    print(y)