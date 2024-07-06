# Programa que converte a temperatura de Fahrenheit para Celsius

# Pede ao usuário para inserir a temperatura em Fahrenheit
fahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))

# Converte a temperatura para Celsius usando a fórmula
celsius = 5 * ((fahrenheit - 32) / 9)

# Mostra a temperatura em graus Celsius
print(f"A temperatura em graus Celsius é {celsius:.2f}°C.")

