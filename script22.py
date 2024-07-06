import matplotlib.pyplot as plt

# Dados fictícios
labels = ['Maçãs', 'Laranjas', 'Bananas', 'Morangos']
quantidades = [30, 25, 15, 20]

# Criando o gráfico de setor
plt.figure(figsize=(8, 6))
plt.pie(quantidades, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Frutas')
plt.axis('equal')  # Faz com que o gráfico seja desenhado como um círculo

# Exibindo o gráfico
plt.show()
