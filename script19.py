import matplotlib.pyplot as plt
import numpy as np

# Gerando dados para os gráficos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
categories = ['A', 'B', 'C', 'D']
values = [7, 13, 5, 17]
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50) * 100
sizes = np.random.rand(50) * 100

# Criando os gráficos
plt.figure(figsize=(12, 4))

# Gráfico de linha
plt.subplot(1, 3, 1)
plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='green', linestyle='dashed')
plt.title('Gráfico de Linha')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Gráfico de barras
plt.subplot(1, 3, 2)
plt.bar(categories, values, color='orange')
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Gráfico de dispersão
plt.subplot(1, 3, 3)
plt.scatter(x_scatter, y_scatter, s=sizes, alpha=0.5, color='red')
plt.title('Gráfico de Dispersão')
plt.xlabel('X')
plt.ylabel('Y')

# Ajustando o layout para melhor visualização
plt.tight_layout()

# Exibindo os gráficos
plt.show()
