# Programa que calcula o peso ideal com base na altura

# Pede ao usuário para inserir a altura
altura = float(input("Informe a sua altura em metros: "))

# Calcula o peso ideal usando a fórmula
peso_ideal = (72.7 * altura) - 58

# Mostra o peso ideal para o usuário
print(f"O seu peso ideal é {peso_ideal:.2f} kg.")
