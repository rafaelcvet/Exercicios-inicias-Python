listaClientes = ["Jose","Pedro","Rafael","Amanda"]

while True:
    print("---------------------------")
    print("1 - Novo Cliente")
    print("2 - Atender Cliente")
    acao=int(input("Qual opção deseja Escolher? "))

    if acao == 1:
        print("fila de atendimento:",listaClientes)
        novoCliente=input("Novo Cliente")
        listaClientes.append(novoCliente)
        print("Cliente Cadastrado com sucesso")
        print("---------------------------")
    if acao == 2:
        for cliente in listaClientes:
            while True:
                print("Atendendo",cliente)
                flag=int(input("Digite 0 Para Encerrar o Atendimento "))
                print("---------------------------")
                print("Fila de Atendimento:",listaClientes)
                if flag == 0:
                    del(listaClientes[0])
                    print("Nova Fila de Atendimento:",listaClientes)
                    break
            break 