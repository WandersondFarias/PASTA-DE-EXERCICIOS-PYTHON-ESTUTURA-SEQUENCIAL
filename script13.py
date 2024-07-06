def calcular_peso_ideal():
    try:
        altura = float(input("Informe a sua altura em metros: "))
        
        if altura <= 0:
            print("Por favor, insira uma altura válida (maior que 0).")
            return
        
        sexo = input("Informe o seu sexo (M para masculino, F para feminino): ").strip().upper()
        
        if sexo == 'M':
            peso_ideal = (72.7 * altura) - 58
            print(f"O seu peso ideal é {peso_ideal:.2f} kg.")
        elif sexo == 'F':
            peso_ideal = (62.1 * altura) - 44.7
            print(f"O seu peso ideal é {peso_ideal:.2f} kg.")
        else:
            print("Sexo inválido. Por favor, insira 'M' para masculino ou 'F' para feminino.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido para a altura.")

calcular_peso_ideal()
