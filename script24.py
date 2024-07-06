import matplotlib.pyplot as plt

# Dados fictícios de notas e status (aprovado ou reprovado)
notas = [7.5, 5.8, 6.9, 4.2, 8.1, 3.5, 6.0, 9.2, 2.8, 7.7]
aprovados = [True, False, True, False, True, False, True, True, False, True]

# Contagem de aprovados e reprovados
aprovados_count = sum(aprovados)
reprovados_count = len(aprovados) - aprovados_count

# Labels para o gráfico
labels = ['Aprovados', 'Reprovados']
sizes = [aprovados_count, reprovados_count]
colors = ['#66b3ff', '#ff9999']
explode = (0.1, 0)  # explode 1st slice (aprovados)

# Plotagem do gráfico
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Porcentagem de Alunos Aprovados e Reprovados')
plt.axis('equal')  # Equal aspect ratio garante que o gráfico seja um círculo.
plt.show()
