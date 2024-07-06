def calcular_multa_pesca():
    try:
        peso = float(input("Informe o peso dos peixes em quilos: "))
        
        if peso < 0:
            print("Por favor, insira um valor de peso válido (maior ou igual a 0).")
            return
        
        limite = 50.0
        multa_por_quilo = 4.0
        
        if peso > limite:
            excesso = peso - limite
            multa = excesso * multa_por_quilo
        else:
            excesso = 0.0
            multa = 0.0
        
        print(f"Peso total de peixes: {peso:.2f} kg")
        print(f"Excesso de peso: {excesso:.2f} kg")
        print(f"Multa a pagar: R$ {multa:.2f}")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido para o peso dos peixes.")

calcular_multa_pesca()
