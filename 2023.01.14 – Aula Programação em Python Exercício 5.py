a=1
while a>0:
  print('{:=^60}'.format("Exercício - Fluxograma"))
  n1 = int(input("Digite o Primeiro Número :"))
  n2 = int(input("Digite o Segundo Número :"))
  n3 = int(input("Digite o Terceiro Número: "))
  soma = n1 + n2 + n3
  if n1>n2 and n1>n3:
    print("O Maior Número é: ",n1)
  elif n2>n1 and n2>n3:
    print("O Maior Número é: ",n2)
  elif n3>n2 and n3>n1:
    print("O Maior Número é: ",n3)
  elif n1==n2 and n1==n3:
    print("Digite Números Diferentes")
  print("A soma dos Números é: ",soma)
  print('{:-^60}'.format("Final do Exercício"))
