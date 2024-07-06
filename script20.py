import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criando o gráfico de linhas
plt.figure(figsize=(8, 5))  # Tamanho da figura (opcional)
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Série A')  # Definindo marcadores, linha e cor
plt.title('Gráfico de Linhas')  # Título do gráfico
plt.xlabel('Eixo X')  # Rótulo do eixo x
plt.ylabel('Eixo Y')  # Rótulo do eixo y
plt.legend()  # Mostra a legenda
plt.grid(True)  # Mostra as grades de fundo (opcional)
plt.show()  # Mostra o gráfico
# Dados para o gráfico
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]

# Criando o gráfico de barras
plt.figure(figsize=(8, 5))  # Tamanho da figura (opcional)
plt.bar(categorias, valores, color='g', alpha=0.6)  # Definindo a cor das barras e a transparência
plt.title('Gráfico de Barras')  # Título do gráfico
plt.xlabel('Categorias')  # Rótulo do eixo x
plt.ylabel('Valores')  # Rótulo do eixo y
plt.grid(axis='y')  # Mostra as grades no eixo y (opcional)
plt.show()  # Mostra o gráfico
import numpy as np

# Dados para o gráfico
x = np.random.rand(50)
y = np.random.rand(50)
cores = np.random.rand(50)
tamanhos = 1000 * np.random.rand(50)

# Criando o gráfico de dispersão
plt.figure(figsize=(8, 5))  # Tamanho da figura (opcional)
plt.scatter(x, y, s=tamanhos, c=cores, alpha=0.5, cmap='viridis')  # Definindo tamanho, cor e transparência
plt.title('Gráfico de Dispersão')  # Título do gráfico
plt.xlabel('Eixo X')  # Rótulo do eixo x
plt.ylabel('Eixo Y')  # Rótulo do eixo y
plt.colorbar()  # Mostra a barra de cores (opcional)
plt.show()  # Mostra o gráfico
