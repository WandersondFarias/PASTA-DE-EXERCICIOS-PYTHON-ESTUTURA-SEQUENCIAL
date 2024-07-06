# Pedir uma letra ao usuário
letra = input("Digite uma letra (F ou M): ")

# Verificar se a letra é "F" ou "M"
if letra.upper() == "F":
    print("F - Feminino")
elif letra.upper() == "M":
    print("M - Masculino")
else:
    print("Letra inválida!")


# Este código utiliza a função input()de pedir uma letra ao usuário, e \
# então verifica se a letra é igual a "F" ou "M" (ignorando se a letra é matemática\
# ou maiúscula, graças ao método upper()). Em seguida, imprima uma mensagem na tela indicando \
# se a letra é "F" (Feminino) ou "M" (Masculino), ou se a letra é inválida.
# Você pode executar este código em um interpretador Python ou salvá-lo \
# em um arquivo com extensão .pye salvá-lo como um script.                                                                          \    