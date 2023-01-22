#transformar em função 
#colar no exercício da senha
def teste():
    print("Escolha 2 números aleatoriamente")
    num1 = int(input("Escolha o Primeiro número:"))
    print("Seu número escolhido foi: ",num1)
    print("Está correto?")#colocar pergunta se sim ou não)

    num2 = int(input("Escolha o Segundo número:"))
    print("Seu número escolhido foi: ",num2)
    print("Está correto?")#colocar pergunta se sim ou não)
    print('{:=^60}'.format(""))
    print("a soma dos números é:",num1 + num2)
    print("a média dos números é:",(num1 + num2)/2)
    print("o produto dos números é:",num1 * num2)

    #criar condicional para divisão
    #colocar 2 possibildades, maior como divisor e maior como denominador
    #se x for maior que y - 

    if num1 > num2:
        print("a divisão do maior pelo menor é:", num2/num1)
    if num1 < num2:
        print("a divisão do maior pelo menor é:", num1/num2)

    if num1 > num2:
        print("a divisão do menor pelo maior é:", num2/num1)
    else:
        print("a divisão do menor pelo maior é:", num1/num2)
teste()