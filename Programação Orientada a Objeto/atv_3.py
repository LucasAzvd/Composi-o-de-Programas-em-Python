class Item:
    def __init__(self, __nome, __valor):
        self.__nome = __nome
        self.__valor = __valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor

class Livro(Item):
    def __init__(self, nome, valor):
        self.tipo = 'L'
        super().__init__(nome, valor)
        self.valor_desconto = valor*0.97

class Brinquedo(Item):
    def __init__(self, nome, valor):
        self.tipo = 'B'
        super().__init__(nome, valor)
        self.valor_desconto = valor*0.95

class Eletronico(Item):
    def __init__(self, nome, valor):
        self.tipo = 'E'
        super().__init__(nome, valor)
        self.valor_desconto = valor*0.92

    
class CestaCompras:
    def __init__(self, **itens):
        self.valor_total_compra_desconto = 0
        self.itens = dict()

    def adicionar_item(self, item_obj, qtde):
        self.itens[item_obj] = qtde
        valor_produtos = qtde * item_obj.valor_desconto
        self.valor_total_compra_desconto += valor_produtos 

    def relatorio_final(self):
        print(round(self.valor_total_compra_desconto, 2))

        for item, qtde in self.itens.items():
            result = ''
            if item.tipo == 'E':
                result += 'Eletronico, '
            elif item.tipo == 'L':
                result += 'Livro, '
            else:
                result += 'Brinquedo, '
            result+= item.nome+', '
            result+= str(qtde)+', '
            result+= f'{item.valor:.2f}, '
            result+= f'{item.valor*qtde:.2f}, '
            result+= f'{(item.valor_desconto*qtde):.2f}'
            print(result)