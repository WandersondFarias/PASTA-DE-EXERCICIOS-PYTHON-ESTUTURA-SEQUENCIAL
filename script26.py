# Classe para representar um produto de calçado
class Produto:
    def __init__(self, codigo, nome, preco, estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def __str__(self):
        return f"Código: {self.codigo} | Nome: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque} unidades"


# Classe para representar a loja
class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        print(f"Produtos disponíveis na loja {self.nome}:")
        for produto in self.produtos:
            print(produto)
        print()

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None


# Classe para representar o carrinho de compras
class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        self.itens.append((produto, quantidade))

    def remover_item(self, produto):
        self.itens = [(p, q) for p, q in self.itens if p != produto]

    def calcular_total(self):
        total = 0.0
        for produto, quantidade in self.itens:
            total += produto.preco * quantidade
        return total

    def listar_items(self):
        print("Itens no carrinho:")
        for produto, quantidade in self.itens:
            print(f"Produto: {produto.nome} | Quantidade: {quantidade}")
        print()


# Função principal para simular a interação do usuário
def main():
    # Criando uma loja
    minha_loja = Loja("Super Calçados")

    # Adicionando alguns produtos à loja
    minha_loja.adicionar_produto(Produto(1, "Tênis Nike Air Max", 299.99, 50))
    minha_loja.adicionar_produto(Produto(2, "Botas Timberland", 399.99, 30))
    minha_loja.adicionar_produto(Produto(3, "Sandálias Havaianas", 49.99, 100))

    # Criando um carrinho de compras
    meu_carrinho = Carrinho()

    # Exibindo os produtos disponíveis
    minha_loja.listar_produtos()

    # Simulando a compra de alguns produtos
    meu_carrinho.adicionar_item(minha_loja.buscar_produto(1), 2)
    meu_carrinho.adicionar_item(minha_loja.buscar_produto(3), 1)

    # Exibindo os itens no carrinho
    meu_carrinho.listar_items()

    # Calculando o total da compra
    total = meu_carrinho.calcular_total()
    print(f"Total da compra: R${total:.2f}")

    # Limpando o carrinho após a compra
    meu_carrinho = Carrinho()
    print("Carrinho limpo após a compra:")
    meu_carrinho.listar_items()

if __name__ == "__main__":
    main()
