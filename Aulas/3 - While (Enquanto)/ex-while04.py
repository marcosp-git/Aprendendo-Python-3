saldo = 1000.00  # Define o saldo inicial da conta

# Inicia um loop infinito que continuará até que o usuário escolha a opção de sair
while True:

    # Imprime as opções do menu disponíveis para o usuário
    print("\nCaixa Eletrônico")
    print("1 - Verificar Saldo")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Sair")

    opcao = input("Escolha uma opção (1-4): ")  # Solicita que o usuário escolha uma opção

    # Verifica a opção escolhida pelo usuário e executa a ação correspondente
    if opcao == '1':

        print(f"Seu saldo é: R$ {saldo:.2f}")  # Imprime o saldo atual da conta

    elif opcao == '2':

        deposito = float(input("Digite o valor do depósito: R$ "))  # Solicita o valor do depósito

        if deposito > 0:  # Verifica se o valor do depósito é positivo

            # saldo = saldo + deposito
            saldo += deposito  # Adiciona o valor do depósito ao saldo
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")  # Confirma o depósito

        else:

            print("Valor de depósito inválido.")  # Informa que o valor do depósito é inválido

    elif opcao == '3':

        saque = float(input("Digite o valor do saque: R$ "))  # Solicita o valor do saque

        if saque > 0 and saque <= saldo:  # Verifica se o valor do saque é válido e se há saldo suficiente

            saldo -= saque  # Subtrai o valor do saque do saldo

            print(f"Saque de R$ {saque:.2f} realizado com sucesso!")  # Confirma o saque

        else:

            print(
                "Valor de saque inválido ou saldo insuficiente.")  # Informa que o valor do saque é inválido ou que não há saldo suficiente

    elif opcao == '4':

        print( "Obrigado por utilizar o nosso caixa eletrônico. Até mais!")  # Agradece o usuário e prepara-se para sair do loop

        break  # Sai do loop, terminando o programa

    else:

        print("Opção inválida. Por favor, tente novamente.")  # Informa ao usuário que ele escolheu uma opção inválida e continua o loop
