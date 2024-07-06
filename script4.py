# Programa que pede as 4 notas bimestrais e mostra a média

# Pede ao usuário para inserir as quatro notas
nota1 = float(input("Informe a primeira nota bimestral: "))
nota2 = float(input("Informe a segunda nota bimestral: "))
nota3 = float(input("Informe a terceira nota bimestral: "))
nota4 = float(input("Informe a quarta nota bimestral: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Mostra a média das notas
print(f"A média das notas bimestrais é {media:.2f}.")
