from abc import ABC, abstractmethod


class ContaCliente(ABC):  # ‘Abstract’ class (O Python utiliza um módulo chamado abc para definir uma classe como abstrata)

    def __init__(self, numero, iof, ir, valor_investido, taxa_rendimento):
        self.numero = numero
        self.iof = iof
        self.ir = ir
        self.valor_investido = valor_investido
        self.taxa_rendimento = taxa_rendimento

    @abstractmethod
    def calculo_rendimento(self):
        pass

    def extrato(self):
        print(f"O saldo atual da conta {self.numero} é R${self.valor_investido:1.2f}")
