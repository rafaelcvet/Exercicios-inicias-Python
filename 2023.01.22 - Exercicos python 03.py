lista = ['azul','verde','roxo']
#while
#index = contador
index = 0 
while index < len(lista): #enquanto index(Contador) for menor que o tamanho da lista
  elemento = lista[index]
  if elemento == 'azul':
    print (elemento)
  elif elemento == 'verde':
    index += 1
    print(elemento)
    continue
  else:
    print (elemento)
  index += 1
