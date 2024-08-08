from src.app.object_oriented.banco.Conta import Conta
from src.app.object_oriented.banco.ContaPoupanca import ContaPoupanca


class ContaRemuneradaPoupanca(Conta, ContaPoupanca):

    def __init__(self, taxa_remuneracao, clientes, numero, saldo, taxa):
        Conta.__init__(self, clientes, numero, saldo)
        ContaPoupanca.__init__(self, taxa_remuneracao)
        self.taxa = taxa

    def calcular_remuneracao_conta(self):
        self.saldo += self.saldo * (self.taxa / 30)
        self.saldo -= self.taxa
