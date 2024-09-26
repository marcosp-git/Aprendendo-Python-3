# Define o número secreto que o usuário deve adivinhar
numero_secreto = 7

# Solicita ao usuário para inserir um número inteiro entre 1 e 10
chute = int(input("Tente adivinhar o número secreto entre 1 e 10: "))

# Verifica se o número inserido pelo usuário é igual ao número secreto
if chute == numero_secreto:

    # Se o usuário adivinhar corretamente, imprime uma mensagem de sucesso
    print("Parabéns! Você adivinhou o número secreto.")

# else - Senão
else:

    # Se o usuário adivinhar errado, imprime uma mensagem de erro
    print("Desculpe, você não adivinhou o número secreto. Tente novamente!")
