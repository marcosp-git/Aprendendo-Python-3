# Solicita as 4 notas bimestrais ao usuário
n1 = float(input("Nota do 1º Bimestre: "))
n2 = float(input("Nota do 2º Bimestre: "))
n3 = float(input("Nota do 3º Bimestre: "))
n4 = float(input("Nota do 4º Bimestre: "))

# Calcula e exibe a média das notas
media = (n1 + n2 + n3 + n4) / 4
print(f"Média: {media}")

# Encontra e exibe a maior e menor nota
maior = max(n1, n2, n3, n4)
menor = min(n1, n2, n3, n4)
print(f"A maior nota do aluno foi {maior} e a menor foi {menor}")

# Com base na média, determina a situação acadêmica do aluno
# Se a média for maior ou igual a 7, o aluno está aprovado
# Se a média for maior ou igual a 5 e menor que 7, o aluno está em recuperação
# Se a média for menor que 5, o aluno está reprovado
if media >= 7:
    print("Aprovado!")  # Imprime na tela que o aluno está aprovado
elif media >= 5:
    print("Recuperação!")  # Imprime na tela que o aluno está em recuperação
else:
    print("Reprovado!")  # Imprime na tela que o aluno está reprovado

