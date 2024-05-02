menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = "Extrato: \n\n"

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor que deseja depositar: R$ "))
        if deposito <= 0:
            print("Valor inválido!")
        else:
            saldo += deposito
            extrato += "Valor de R$ " + str("{:.2f}".format(deposito)) + " depositado\n"
            

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque > 0:
                if saque > 500:
                    print("Valor acima do limite!")
                else: 
                    if saldo < saque:
                        print("Você não possui saldo suficiente!")
                    else:
                        print("Valor de R$ " + str("{:.2f}".format(saque)) + " sacado com sucesso!")
                        extrato += "Valor de R$ " + str("{:.2f}".format(saque)) + " sacado\n"
                        saldo -= saque
                        numero_saques += 1
            else:
                print("Valor inválido!")
        else:
            print("Você atingiu sua quantidades de saques diárias!")


    elif opcao == "e":
        print(extrato + "Saldo atual: R$ "+str("{:.2f}".format(saldo)))

    elif opcao == "q":
        break

    else:
        print("Comando inválido!")