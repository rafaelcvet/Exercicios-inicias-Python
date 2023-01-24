#exercício de senha + programa
usuario = ["admin"]
senha = ["12345"]
print('{:=^60}'.format("Exercício 5 - Senha"))
entrar_usuario = str(input("Digite o usuário: "))
while not entrar_usuario in usuario:
    entrar_usuario = str(input("Usuário não existe: "))
entrar_senha = str(input("Digite sua senha: "))
while not entrar_senha in senha:
    entrar_usuario(str(input("Senha Errada!")))
else:
    print("Seja Bem Vindo:",usuario)
    
print('{:=^60}'.format("Exercício 5 - Comparação"))
print("Escolha 2 números aleatoriamente")
print("Pense no Primeiro Número! ")
print(" ")
num1 = int(input("Escreva o Primeiro Número Escolhido: "))
print("Seu número escolhido foi: ",num1)

r1 = input("O Primeiro Número Está Correto? - y/n: ")
#--------------------
print('{:=^60}'.format(""))
while not r1=="y":
    print("Reinicie o programa!")
else:
    print("Vamos Continuar, Pense em um Segundo Número!")
#--------------------
print('{:=^60}'.format(""))
num2 = int(input("Escreva o Segundo Número Escolhido: "))
print("Seu número escolhido foi: ",num2)
print("Está correto?")#colocar pergunta se sim ou não)
r2 = input("O Segundo Número Está Correto? - y/n: ")
while not r2=="y":
    print("Reinicie o programa!")
else:
    print("Vamos Continuar!")
#--------------------
print('{:=^60}'.format(""))
print("a soma dos números é: ",num1 + num2)
print('{:=^60}'.format(""))
print("a média dos números é: ",(num1 + num2)/2)
print('{:=^60}'.format(""))
print("o produto dos números é: ",num1 * num2)

if num1 > num2:
    print("a divisão do maior pelo menor é:", num2/num1)
if num1 < num2:
    print("a divisão do maior pelo menor é:", num1/num2)

if num1 > num2:
    print("a divisão do menor pelo maior é:", num1/num2)
else:
    print("a divisão do menor pelo maior é:", num2/num1)