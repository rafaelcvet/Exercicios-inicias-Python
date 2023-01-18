print('{:=^60}'.format("Exercício - Aula Programação em Python"))
x = int(input("Digite a variavel X\n"))
print("Voçê escolheu o número \n", x)
y = int(input("Digite a Variável Y\n"))
print("Voçê escolheu o número \n", y)
if (x>y):
  print("x maior que y")
elif (y>x):
  print("y maior que x")
else:
  print("x é igual a y")
  
  
#este exercício retorna como erro ao final caso não se denomine um número para x ou y