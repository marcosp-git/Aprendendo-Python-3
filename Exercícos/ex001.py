# Solicita ao usuário que insira um número (float)
n1 = float(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if n1 % 2 == 0:
    print(f"O número {n1} é par.")  # Imprime que o número é par
else:
    print(f"O número {n1} é ímpar.")  # Imprime que o número é ímpar

# Verifica se o número é positivo, negativo ou zero
if n1 > 0:
    raiz = n1 ** 0.5  # Calcula a raiz quadrada do número caso positivo
    print(f"O número {n1:.0f} é positivo e sua raiz quadrada é {raiz:.0f}.")  # Imprime que o número é positivo e sua raiz quadrada
elif n1 < 0:
    print(f"O número {n1} é negativo.")  # Imprime que o número é negativo
else:
    print("O número informado é 0.")  # Imprime que o número é zero
