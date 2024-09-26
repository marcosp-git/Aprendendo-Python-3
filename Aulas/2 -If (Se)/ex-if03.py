nota = int(input("Por favor, digite a nota do estudante (0-100): "))

# Verifica em qual categoria a nota se encaixa
if nota >= 90 and nota <= 100:

    print("Excelente!")

elif nota >= 70 and nota <= 89:

    print("Bom!")

elif nota >= 50 and nota <= 69:

    print("Satisfatório!")

else:

    print("Insuficiente!")
    