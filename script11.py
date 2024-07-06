# Programa que pede 2 números inteiros e 1 número real e realiza cálculos específicos

# Pede ao usuário para inserir os números
num_inteiro1 = int(input("Informe o primeiro número inteiro: "))
num_inteiro2 = int(input("Informe o segundo número inteiro: "))
num_real = float(input("Informe um número real: "))

# Calcula o produto do dobro do primeiro com metade do segundo
produto = (2 * num_inteiro1) * (num_inteiro2 / 2)

# Calcula a soma do triplo do primeiro com o terceiro
soma = (3 * num_inteiro1) + num_real

# Calcula o terceiro número elevado ao cubo
cubo = num_real ** 3

# Mostra os resultados
print(f"O produto do dobro do primeiro com metade do segundo é {produto}.")
print(f"A soma do triplo do primeiro com o terceiro é {soma}.")
print(f"O terceiro número elevado ao cubo é {cubo}.")
