# Inicia loop para manter o programa rodando até o usuário decidir sair
while True:
    print("\nCalculadora simples:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    # Receber a escolha do usuário
    escolha = int(input("Escolha uma operação(1-5): "))

    # Condição para sair do programa
    if escolha == 5:
        print("Até mais!")
        break

    # Receber os dois números para a operação
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    # Condição para Adição
    if escolha == 1:
        resultado = n1 + n2
        print("Resultado: ", resultado)

    # Condição para subtração
    elif escolha == 2:
        resultado = n1 - n2
        print("Resultado: ", resultado)

    # Condição para multiplicação
    elif escolha == 3:
        resultado = n1 * n2
        print("Resultado: ", resultado)

    # Condição para divisão
    elif escolha == 4:

        # Verificar se o divisor é zero para evitar erro de divisão por zero
        if n2 != 0:
            resultado = n1 / n2
            print("Resultado: ", resultado)

        # Mensagem de erro para divisão por zero
        else:
            print("Erro: Divisão por zero.")

    # Condição para opção inválida
    else:
        print("Opção inválida. Tente novamente!")
