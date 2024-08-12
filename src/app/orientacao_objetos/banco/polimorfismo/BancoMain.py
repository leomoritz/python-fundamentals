from src.app.orientacao_objetos.banco.polimorfismo.Banco import Banco
from src.app.orientacao_objetos.banco.polimorfismo.ContaComum import ContaComum
from src.app.orientacao_objetos.banco.polimorfismo.ContaRemunerada import ContaRemunerada

banco = Banco(1, 'Banco do Brasil')
conta_comum = ContaComum(2, 0.01, 0.1, 2000, 0.05)
conta_remunerada = ContaRemunerada(3, 0.01, 0.1, 2000, 0.05)

banco.adicionar_conta(conta_comum)
banco.adicionar_conta(conta_remunerada)
banco.calcular_rendimento_mensal()
banco.imprime_saldo_contas()
