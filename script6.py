import math

# Programa que calcula a área de um círculo

# Pede ao usuário para inserir o raio do círculo
raio = float(input("Informe o raio do círculo: "))

# Calcula a área do círculo
area = math.pi * raio ** 2

# Mostra a área do círculo
print(f"A área do círculo com raio {raio} é {area:.2f}.")
