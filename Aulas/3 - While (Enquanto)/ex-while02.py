# Inicializa a variável para armazenar a soma dos números digitados com 0
somaNumerosDigitados = 0

# Solicita ao usuário que digite um número ou 0 para sair do loop
numero = int(input("Digite um número ou 0 para sair: "))

# Continua o loop enquanto o número digitado for diferente de 0
while numero != 0:
    # Adiciona o número digitado à soma total
    # somaNumerosDigitados = somaNumerosDigitados + numero
    somaNumerosDigitados += numero

    # Solicita ao usuário que digite um número novamente ou 0 para sair
    numero = int(input("Digite um número ou 0 para sair: "))

# Imprime a soma total dos números digitados depois que o loop termina
print("Total: ", somaNumerosDigitados)
