from typing import List

from src.app.object_oriented.banco.polimorfismo import ContaCliente


class Banco:

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionar_conta(self, conta: ContaCliente):
        self.contas.append(conta)

    def calcular_rendimento_mensal(self):
        for conta in self.contas:
            conta.calculo_rendimento()

    def imprime_saldo_contas(self):
        for conta in self.contas:
            conta.extrato()