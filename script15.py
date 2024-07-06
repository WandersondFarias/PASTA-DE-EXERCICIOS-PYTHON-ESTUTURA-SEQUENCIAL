def calcular_salario():
    try:
        # Solicita ao usuário que informe o valor ganho por hora e o número de horas trabalhadas no mês
        valor_hora = float(input("Informe quanto você ganha por hora: R$ "))
        horas_mes = float(input("Informe quantas horas você trabalhou no mês: "))
        
        # Calcula o salário bruto
        salario_bruto = valor_hora * horas_mes
        
        # Calcula os descontos
        ir = 0.11 * salario_bruto  # 11% de Imposto de Renda
        inss = 0.08 * salario_bruto  # 8% de INSS
        sindicato = 0.05 * salario_bruto  # 5% para o sindicato
        
        # Calcula o salário líquido
        salario_liquido = salario_bruto - ir - inss - sindicato
        
        # Exibe os resultados formatados
        print(f"+ Salário Bruto : R$ {salario_bruto:.2f}")
        print(f"- IR (11%) : R$ {ir:.2f}")
        print(f"- INSS (8%) : R$ {inss:.2f}")
        print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
        print(f"= Salário Líquido : R$ {salario_liquido:.2f}")
        
    except ValueError:
        print("Valor inválido. Certifique-se de inserir números válidos para o valor por hora e horas trabalhadas.")

# Chamada da função para calcular o salário
calcular_salario()
