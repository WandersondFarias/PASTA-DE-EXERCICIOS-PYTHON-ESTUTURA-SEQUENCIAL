# Programa que calcula o salário mensal com base no ganho por hora e nas horas trabalhadas

# Pede ao usuário para inserir o valor ganho por hora
valor_hora = float(input("Informe quanto você ganha por hora: "))

# Pede ao usuário para inserir o número de horas trabalhadas no mês
horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))

# Calcula o salário mensal
salario_mensal = valor_hora * horas_trabalhadas

# Mostra o salário mensal para o usuário
print(f"O salário mensal é R$ {salario_mensal:.2f}.")
