menu = '''
Seja bem-vindo(a) ao banco Python, aqui nosso foco é simplificar a sua vida!
giO que deseja fazer hoje?
[ 1 ] Depositar
[ 2 ] Sacar
[ 3 ] Extrato
[ 4 ] Empréstimo
[ 5 ] Sair
=>  '''

saldo = 0
limite = 500
extrato = ""
emprestimo = 600
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$"))

        if valor > 0:
            saldo += valor
            extrato +=f"Depósito: R$ {valor:.2f}\n"
            print(f"Seu deposito de R${valor:.2f} foi efetuado com sucesso!")

        else:
            print("A operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe quanto você deseja sacar: R$"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("A operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("A operação falhou! O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("A operação falhou! Você excedeu o número máximo de saques diários, tente novamente amanhã.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Operação realizada com sucesso! \nVocê sacou R${valor:.2f}")

        else:
            print("A operação falhou! O Valor informado é inválido.")

    elif opcao == "3":
        print("\n============= EXTRATO =============")
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================")

    elif opcao == "4":
        credito_disponivel = saldo + (0.5 * saldo)
        print(f"Você tem disponível: R$ {credito_disponivel:.2f} de crédito para emprestimos")

        adquirir_emprestimo = input("Deseja adquirir esse empréstimo? (sim/não): ").strip().lower()

        if adquirir_emprestimo == "sim":
            print("Entre em contato com o seu gerente do banco, ele irá te auxiliar nesse procedimento")
        
        elif adquirir_emprestimo == "não":
            continue
        
        else:
            print("Resposta inválida. Retornando ao menu principal.")

    elif opcao == "5":
            print("O Banco Python agradece por utilizar nossos serviços. Até logo!")
            break 
