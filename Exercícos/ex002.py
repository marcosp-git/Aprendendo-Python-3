# Solicia ao usuário que insira 2 números (float)
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Calcula e mostra a soma dos dois números
soma = n1 + n2
print(f"\nA soma entre {n1} e {n2} é: {soma}.")

# Calcula e mostra a subtração do primeiro número pelo segundo
sub = n1 - n2
print(f"A subtração de {n1} por {n2} é: {sub}.")

# Calcula e mostra a multiplicação dos dois números
mult = n1 * n2
print(f"A multiplicação entre {n1} e {n2} é: {mult}.")

# Verifica se o segundo número é zero antes de tentar dividir
if n2 != 0:
    div = n1 / n2
    print(f"A divisão de {n1} por {n2} é: {div:.2f}.")  # Imprime na tela a divisão
else:
    print(f"Divisão inválida! Não é possivel dividir {n1} por zero.")  # Imprime na tela caso a divisão seja inválida

# Verifica se algum dos números (ou ambos) é igual a zero
if n1 == 0 and n2 == 0:
    print("Os dois números são iguais a zero.")  # Imprime na tela caso os dois números seja iguais a zero
elif n1 == 0:
    print("O primeiro número é igual a zero.")  # Imprime na tela caso o primeiro número seja igual a zero
elif n2 == 0:
    print("O segundo número é igual a zero.")  # Imprime na tela caso o segundo número seja igual a zero
else:
    print("Nenhum número é igual a zero")  # Imprime na tela caso nenhum dos números seja igual a zero

# Calcula e mostra a média dos dois números
media = soma / 2
print(f"A média entre {n1} e {n2} é: {media}.")

# Compara os dois números
if n1 > n2:
    print(f"{n1} é maior que {n2}.")  # Imprime na tela caso o primeiro número seja maior que o segundo
elif n2 > n1:
    print(f"{n2} é maior que {n1}")  # Imprime na tela caso o segundo número seja maior que o primeiro
else:
    print("Os dois números são iguais.")  # Imprime na tela caso os números sejam iguais
