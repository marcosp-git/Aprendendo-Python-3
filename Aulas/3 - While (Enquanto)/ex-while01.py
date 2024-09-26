# Define a senha correta do sistema como "123"
senhaSistema = "123"

# Solicita ao usuário que digite a senha
senhaDigitada = input("Digite sua senha: ")

# Continua o loop enquanto a senha digitada pelo usuário for diferente da senha correta do sistema
while (senhaSistema != senhaDigitada):
    # Imprime uma mensagem indicando que a senha está incorreta
    print("Senha incorreta, tente novamente!")

    # Solicita ao usuário que digite a senha novamente
    senhaDigitada = input("\nDigite sua senha: ")

# Imprime uma mensagem de sucesso quando o usuário digita a senha correta e o loop termina
print("\nMuito bem! Você digitou a senha correta!")
