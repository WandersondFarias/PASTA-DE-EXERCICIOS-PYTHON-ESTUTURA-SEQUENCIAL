import math

def calcular_tinta():
    try:
        # Solicita ao usuário que informe o tamanho da área a ser pintada em metros quadrados
        area = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))
        
        if area <= 0:
            print("Por favor, informe um valor válido para a área.")
            return
        
        # Cálculo da quantidade de tinta necessária (em litros)
        litros_tinta = area / 6 * 1.1  # considerando 10% de folga
        
        # Cálculo da quantidade de latas de 18 litros necessárias e seu preço total
        latas18 = math.ceil(litros_tinta / 18)
        preco_latas18 = latas18 * 80.0
        
        # Cálculo da quantidade de galões de 3,6 litros necessários e seu preço total
        galoes36 = math.ceil(litros_tinta / 3.6)
        preco_galoes36 = galoes36 * 25.0
        
        # Cálculo da combinação de latas e galões para minimizar o desperdício de tinta
        latas_combinacao = math.floor(litros_tinta / 18)
        litros_restantes = litros_tinta - latas_combinacao * 18
        galoes_combinacao = math.ceil(litros_restantes / 3.6)
        
        preco_combinacao = (latas_combinacao * 80.0) + (galoes_combinacao * 25.0)
        
        # Exibição dos resultados
        print(f"Para comprar apenas latas de 18 litros:")
        print(f"Quantidade de latas: {latas18}")
        print(f"Preço total: R$ {preco_latas18:.2f}")
        
        print("\nPara comprar apenas galões de 3,6 litros:")
        print(f"Quantidade de galões: {galoes36}")
        print(f"Preço total: R$ {preco_galoes36:.2f}")
        
        print("\nPara misturar latas e galões, minimizando o desperdício:")
        print(f"Quantidade de latas: {latas_combinacao}")
        print(f"Quantidade de galões: {galoes_combinacao}")
        print(f"Preço total: R$ {preco_combinacao:.2f}")
        
    except ValueError:
        print("Valor inválido. Certifique-se de inserir um número válido para a área a ser pintada.")

# Chamada da função para calcular a quantidade de tinta necessária e os preços para cada estratégia
calcular_tinta()
