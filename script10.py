# Programa que converte a temperatura de Celsius para Fahrenheit

# Pede ao usuário para inserir a temperatura em graus Celsius
celsius = float(input("Informe a temperatura em graus Celsius: "))

# Converte a temperatura para Fahrenheit usando a fórmula
fahrenheit = celsius * (9 / 5) + 32

# Mostra a temperatura em graus Fahrenheit
print(f"A temperatura em graus Fahrenheit é {fahrenheit:.2f}°F.")
