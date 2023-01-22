Exercícios de de senha
print('{:=^60}'.format("Exercício 3 - Dados"))
#login e senha validos
login_valido ="Rafael"
senha_valida ="Teste123"
#----------------------------------------------
#colocar função
#----------------------------------------------

#digitar login, caso seja o correto, digitar senha, caso seja correto acesso ao código
login = input("Digite seu Login:")
while True: 
    if login ==login_valido:
        print("Bem vindo", login_valido,"digite sua senha!")
        senha = input("Digite sua senha: ")
        break
        if senha ==senha_valida:
            print("Bem vindo, ",login_valido,"loguin e senha válidos")
            #restante - código
    else:
        print("Usuário e/ou senha inválidos, digite novamente")
    login = input("Digite seu Login:")

#Colocar função para repetir digitar login e senha caso esteja errado