print('{:=^60}'.format("Exercício - Fluxograma"))
  n1 = int(input("Digite o Primeiro Número :\n"))
  n2 = int(input("Digite o Segundo Número :\n"))
  n3 = int(input("Digite o Terceiro Número:\n"))
  lista = [n1, n2, n3]

  soma = n1 + n2 + n3
 
 #----------------------------------------------------
print(max(int(number) for number in lista))

 #----------------------------------------------------    
  print("A soma dos Números é: ",soma)
  print('{:-^60}'.format("Final do Exercício",))
Exercícios 05.3
print('{:=^60}'.format("Exercício - Fluxograma"))
lista = []
numeros = (int(input("Digite a quantidade de números: ")))
soma = 0
for lista in range(numeros):
  lista = int(input("Digire o Número: "))
  soma += lista
 #----------------------------------------------------
print(max(int(number) for number in lista))
 #----------------------------------------------------    
print("A soma dos Números é: ",soma)
print('{:-^60}'.format("Final do Exercício",))
