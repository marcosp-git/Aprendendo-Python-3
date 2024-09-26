# 1. Crie uma variável chamada "frase" e atribua a ela a seguinte
# frase: "Python é uma linguagem de programação poderosa e versátil."

frase = "Python é uma linguagem de programação poderosa e versátil."

# 2. Imprima na tela o tamanho da frase, ou seja, a quantidade de
# caracteres presentes nela.

tamanho_frase = len(frase)
print("Tamanho da frase:", tamanho_frase)

# 3. Crie uma variável chamada "palavra" e atribua a ela a primeira
# palavra da frase.

palavra = frase.split()[0]
print("Primeira palavra da frase:", palavra)

# 4. Converta a variável "frase" para letras maiúsculas e atribua o
# resultado a uma nova variável chamada "frase_maiuscula".

frase_maiuscula = frase.upper()
print("Frase em maiúsculas:", frase_maiuscula)

# 5. Substitua a palavra "poderosa" por "incrível" na variável
# "frase" e atribua o resultado a uma nova variável chamada "frase_substituida".

frase_substituida = frase.replace("poderosa", "incrível")
print("Frase com substituição:", frase_substituida)
