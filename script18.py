def calcular_tempo_download():
    try:
        # Solicita ao usuário que informe o tamanho do arquivo em MB e a velocidade do link em Mbps
        tamanho_arquivo_mb = float(input("Informe o tamanho do arquivo para download em MB: "))
        velocidade_link_mbps = float(input("Informe a velocidade do link de Internet em Mbps: "))
        
        if tamanho_arquivo_mb <= 0 or velocidade_link_mbps <= 0:
            print("Por favor, informe valores válidos maiores que zero.")
            return
        
        # Convertendo o tamanho do arquivo de MB para Mb (1 byte = 8 bits)
        tamanho_arquivo_mbps = tamanho_arquivo_mb * 8
        
        # Calcula o tempo aproximado de download em minutos
        tempo_download_minutos = (tamanho_arquivo_mbps / velocidade_link_mbps) / 60
        
        # Exibição do resultado
        print(f"Tempo aproximado de download: {tempo_download_minutos:.2f} minutos")
        
    except ValueError:
        print("Valor inválido. Certifique-se de inserir números válidos para o tamanho do arquivo e velocidade do link.")

# Chamada da função para calcular o tempo de download
calcular_tempo_download()
