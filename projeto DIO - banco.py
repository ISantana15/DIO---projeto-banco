menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[4] Encerrar

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("informe o valor que deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor}\n"
        else:
            print("A Operação falhou! O valor informado é invalido")
        
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Erro! A conta não possui saldo suficiente.")
        elif excedeu_limite:
            print("Erro! Valor do saque excete o limite permitido.")
        elif excedeu_saques:
            print("Erro! Numero de saques permitidos foi atingido")
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
    elif opcao == "3":
        print("\n----------Extrato----------")
        print("Não foram realizadas movimentações na sua conta." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("-----------------------------")
    elif opcao == "4":
        break
    else:
        print("Opção invalida, selecione uma opçao entre 1 a 4")