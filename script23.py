import matplotlib.pyplot as plt

# Dados fictícios de notas (suponha que são as notas finais de cada aluno)
notas_aprovados = [7.5, 8.2, 6.9, 9.1, 8.5]
notas_reprovados = [4.2, 5.8, 3.5, 6.1, 4.9]

# Definindo os índices dos alunos para o eixo x (apenas para este exemplo)
indices_alunos = range(1, len(notas_aprovados) + 1)

# Criando o gráfico de linhas
plt.figure(figsize=(10, 6))  # Tamanho do gráfico (opcional)

# Plotando as linhas para notas de aprovados e reprovados
plt.plot(indices_alunos, notas_aprovados, marker='o', linestyle='-', color='g', label='Aprovados')
plt.plot(indices_alunos, notas_reprovados, marker='o', linestyle='-', color='r', label='Reprovados')

# Adicionando rótulos e título
plt.xlabel('Alunos')
plt.ylabel('Notas')
plt.title('Notas dos Alunos (Aprovados vs Reprovados)')
plt.xticks(indices_alunos)  # Definindo os ticks do eixo x para os índices dos alunos
plt.legend()  # Mostrando a legenda com as cores e etiquetas definidas

# Exibindo o gráfico
plt.grid(True)  # Habilitando a grade no gráfico (opcional)
plt.tight_layout()  # Ajustando layout
plt.show()
