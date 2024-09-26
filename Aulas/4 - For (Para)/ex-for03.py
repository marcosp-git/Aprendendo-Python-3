# Solicitando ao usuário o número para criar a tabela de multiplicação
N = int(input("Digite um número inteiro positivo para exibir a sua tabela de multiplicação: "))

# Utilizando um loop for para criar a tabela de multiplicação de 1 a 10
for i in range(1, 11):
    resultado = N * i  # Calculando o resultado da multiplicação

    print(f"{N} x {i} = {resultado}")  # Imprimindo o resultado

# Imprimindo uma linha final
print("Fim da tabela de multiplicação.")
