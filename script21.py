import matplotlib.pyplot as plt

# Dados fictícios
categorias = ['A', 'B', 'C', 'D']
valores = [7, 13, 5, 17]

# Criando o gráfico de barras
plt.figure(figsize=(8, 6))  # Define o tamanho da figura (opcional)

plt.bar(categorias, valores, color='skyblue')

# Adicionando título e rótulos aos eixos
plt.title('Exemplo de Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Exibindo o gráfico
plt.show()
