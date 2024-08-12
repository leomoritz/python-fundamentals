from src.app.orientacao_objetos.banco.polimorfismo.ContaCliente import ContaCliente


class ContaComum(ContaCliente):

    def __init__(self, numero, iof, ir, valor_investido, taxa_rendimento):
        super().__init__(numero, iof, ir, valor_investido, taxa_rendimento)

    def calculo_rendimento(self):
        self.valor_investido += (self.valor_investido * self.taxa_rendimento)