# Inicializando a variável resultado com 1
resultado = 1

# Utilizando um loop for para iterar pelos números de 1 a 5
for numero in range(1, 6):

    # Multiplicando o resultado pelo número atual
    resultado *= numero

    print(f"Multiplicando por {numero}, o resultado parcial é {resultado}")

print(f"O resultado final da multiplicação de 1 a 5 é: {resultado}")