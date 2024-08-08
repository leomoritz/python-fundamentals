from Conta import Conta
from src.app.object_oriented.banco.exceptions.ContaOperacaoInvalida import ContaOperacaoInvalida


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        Conta.__init__(self, clientes, numero, saldo) # Chamada ao construtor da superclasse
        self.limite = limite

    def sacar(self, valor):
        saldo_com_limite = self.saldo + self.limite
        if saldo_com_limite < valor:
            raise ContaOperacaoInvalida("Saldo insuficiente para realizar o saque.")
        else:
            self.valida_valor(valor)
            self.saldo = saldo_com_limite - valor
            print("Saque realizado com sucesso!")
            self.extrato.adicionar_transacao("Saque", valor)
