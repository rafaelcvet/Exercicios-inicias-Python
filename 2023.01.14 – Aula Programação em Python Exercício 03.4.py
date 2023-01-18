def aa(str):
  try:
    return int(input(str))
  except:
    exit("erro, insira um número!!")

print('{:=^60}'.format("Exercício - Aula Programação em Python"))
x = aa(input("Digite a variavel X\n"))
print("Voçê escolheu o número \n", x)
y = aa(input("Digite a Variável Y\n"))
print("Voçê escolheu o número \n", y)
if (x>y):
  print("x maior que y")
elif (y>x):
  print("y maior que x")
else:
  print("x é igual a y")

#não consegui rodar, apresentou erro
