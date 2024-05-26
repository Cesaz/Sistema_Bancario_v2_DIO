def menu(): # Menu Para Mostrar As Opções Ao Usuário.
    menu = """ 

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Novo Usuário
    [0] Sair

    => """
    return input(menu)

def deposito(saldo, valor_escolhido, extrato, /): # Função de Deposito.
    if valor_escolhido > 0: # Se o Valor for maior que zero.
        saldo += valor_escolhido
        extrato += f"Depósito: R$ {valor_escolhido:.2f}\n"
        print(f"DEPÓSITO DE R${valor_escolhido:.2f} REALIZADO COM SUCESSO")

    else: # Caso o valor seja igual ou menor que zero.
        print("O valor informado é inválido. Tente Novamente")

    return saldo, extrato

def saque(*, saldo, valor_escolhido, extrato, limite, numero_saque, limite_saques): # Função de Saque.
    saldo_insuficiente = valor_escolhido > saldo # Saldo Insuficiente caso o Valor Escolhido seja Maior que o Saldo.
    limite_insuficiente = valor_escolhido > limite # Limite Insuficiente caso o Valor Escolhido seje Maior que o Limite.
    saque_insuficiente = numero_saque >= limite_saques # Saque Insuficiente caso o Numero do Saque seja Maior ou Igual ao Maximo de Saques permitidos.  
    
    if saldo_insuficiente:
        print("NÃO FOI POSSÍVEL REALIZAR O SAQUE! SALDO INSUFICIENTE.")

    elif limite_insuficiente:
        print("NÃO FOI POSSIVEL REALIZAR O SAQUE! LIMITE ACIMA DO PERMITIDO.")

    elif saque_insuficiente:
        print("NÃO FOI POSSÍVEL REALIZAR O SAQUE! QUANTIDADE MAXIMA DE SAQUES UTILIZADAS.")

    elif valor_escolhido > 0:
        saldo -= valor_escolhido
        extrato += f"Saque: R$ {valor_escolhido:.2f}\n"
        numero_saque += 1
        print(f"SAQUE NO VALOR DE R${valor_escolhido:.2f} REALIZADO COM SUCESSO")

    else:
        print("ALGO DEU ERRADO! TENTE NOVAMENTE.")
        
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato): # Função para mostrar o Extrato.
    if extrato == "": # Caso o Extrato esteja vazio.
        print("Não foram realizadas movimentações.")

    else: # Caso o Extrato possua alguma transação.
        print(extrato)
        print("=======================")
        print(f"SALDO TOTAL => R$ {saldo:.2f}") 
        print("=======================")

def novo_usuario(usuarios): # Função para Criar um Novo Usuário.
    cpf = input("INFORME O CPF: ")
    cpf = cpf.replace('.' '-', '""') # Remove os . e - caso o usuário os digite entre os números.
    usuario = filtrar_usuario(cpf, usuarios) # Verifica se o CPF já está cadastrado.

    if usuario: # Caso o CPF já esteja cadastrado.
        print("JÁ EXISTE UM USUÁRIO COM ESSE CPF!")
        return
    
    # Se o CPF não estiver cadastrado.
    nome = input("INFORME O NOME COMPLETO: ")
    data_nascimento = input("INFORME A DATA DE NASCIMENTO (NO SEGUINTE FORMATO DD-MM-AAAA): ")
    rua = input("INFORME O NOME DA RUA: ")
    numero = input("INFORME O NUMERO: ")
    bairro = input("INFORME O NOME DO BAIRRO: ")
    cidade = input("INFORME O NOME DA CIDADE: ")
    estado = input("INFORME A SIGLA DO ESTADO: ")

    endereco = rua, numero, bairro, cidade, estado

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("USUÁRIO CRIADO COM SUCESSO!") # Adiciona o Usuário Criado na Variavel usuarios.

def filtrar_usuario(cpf, usuarios): # Função para filtrar os Usuários.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] # Verifica se o CPF já existe em Usuario dentro de Usuarios.
    return usuarios_filtrados[0] if usuarios_filtrados else None # Retorna o Usuario caso encontre o CPF existente.

def nova_conta(agencia, numero_conta, usuarios): # Função para Criar uma Nova Conta.
    cpf = input("INFORME O CPF: ")
    cpf = cpf.replace('.' '-', '""') # Remove os . e - caso o usuário os digite entre os números.
    usuario = filtrar_usuario(cpf, usuarios) # Verifica se o CPF já está cadastrado.

    if usuario: # Caso CPF já esteja cadastrado, a conta é criada.
        print("CONTA CRIADA COM SUCESSO!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario} # Adiciona a conta criada na Variavel contas.

    print("USUÁRIO NÃO ENCONTRADO, POR FAVOR UTILIZE A OPÇÃO [5] Novo Usuário")


def principal(): # Função com a parte principal do programa.
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == "1": # Inicia a Função deposito.
            valor_escolhido = input("DIGITE O VALOR DO DEPOSITO: ")
            valor_escolhido = valor_escolhido.replace(',', '.')
            valor_escolhido = float(valor_escolhido)

            saldo, extrato = deposito(saldo, valor_escolhido, extrato)

        elif opcao == "2": # Inicia a Função Saque.
            valor_escolhido = input("QUANTO GOSTARIA DE SACAR?: ")
            valor_escolhido = valor_escolhido.replace(',', '.')
            valor_escolhido = float(valor_escolhido)

            saldo, extrato = saque(
                saldo=saldo,
                valor_escolhido=valor_escolhido,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3": # Inicia a Função mostrar_extrato.
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "4": # Inicia a Função nova_conta.
            numero_conta = len(contas) + 1 # Adiciona um numero diferente a cada conta criada.
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta: # Caso a conta tenha sido criada na Função.
                contas.append(conta) # Adiciona a conta criada na Variavel contas.

        elif opcao == "5": # Inicia a Função novo_usuario.
            novo_usuario(usuarios)
        
        elif opcao == "0":
            break
            
principal()