import math

def calcular_tinta():
    try:
        # Solicita ao usuário que informe o tamanho da área a ser pintada em metros quadrados
        area = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))
        
        if area <= 0:
            print("Por favor, informe um valor válido para a área.")
            return
        
        # Cálculo da quantidade de tinta necessária (em litros)
        litros_tinta = area / 3
        
        # Cálculo da quantidade de latas de tinta necessárias (cada lata tem 18 litros)
        latas_tinta = math.ceil(litros_tinta / 18)  # arredonda para cima usando math.ceil
        
        # Cálculo do preço total das latas de tinta
        preco_total = latas_tinta * 80.0
        
        # Exibição dos resultados
        print(f"Quantidade de latas de tinta necessárias: {latas_tinta}")
        print(f"Preço total: R$ {preco_total:.2f}")
        
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido para a área a ser pintada.")

# Chamada da função para calcular a quantidade de tinta necessária e o preço total
calcular_tinta()
