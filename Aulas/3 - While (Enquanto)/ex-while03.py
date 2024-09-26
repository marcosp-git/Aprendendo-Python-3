# Inicializa a variável 'maiorNumero' com -1 para comparar com os números digitados
maiorNumero = -1

# Solicita ao usuário que digite um número inteiro e maior que zero
numeroDigitado = int(input("Digite um número inteiro e maior que ZERO: "))

# Continua o loop enquanto o número digitado for maior ou igual a 0
while numeroDigitado >= 0:

    # Verifica se o número digitado é maior que o 'maiorNumero' armazenado
    if numeroDigitado > maiorNumero:
        # Atualiza 'maiorNumero' se o número digitado for maior
        maiorNumero = numeroDigitado

    # Solicita ao usuário que digite um novo número inteiro e maior que zero
    numeroDigitado = int(input("Digite um número inteiro e maior que ZERO: "))

# Imprime o 'maiorNumero' após cada entrada; esta linha deve estar fora do loop 'while' para imprimir apenas o resultado final
print("Maior número: ", maiorNumero)
