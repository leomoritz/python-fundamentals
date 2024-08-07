from Conta import Conta
from Cliente import Cliente

print("Bem-vindo ao sistema de contas bancárias.")

print("## Criando conta 1 com conta conjunta...")
cliente_titular_1 = Cliente("João Augusto Fonseca", 887456988788, "Rua 1")
cliente_dependente_1 = Cliente("Maria do Prado", 997854112587, "Rua 1")
clientes = [cliente_titular_1, cliente_dependente_1]
conta_1 = Conta(clientes, 1, 1000)
print("## Imprimindo clientes da conta 1...")
conta_1.imprimir_clientes()
print("## Depositar 500 na conta 1...")
conta_1.depositar(500)
print("## Sacar 200 da conta 1...")
conta_1.sacar(200)
print("## Gerando extrato da conta 1...")
conta_1.gerar_extrato()

print("\n## Criando conta 2 com apenas conta titular...")
cliente_titular_2 = Cliente("Joana", 789, "Rua 2")
conta_2 = Conta(cliente_titular_2, 2, 3000)
print("## Impressão dos clientes da conta 2...")
conta_2.imprimir_clientes()
print("## Transferir 1000 para conta 1...")
conta_2.transferir(2500, conta_1)
print("## Gerando extrato da conta 2 após transferência...")
conta_2.gerar_extrato()
print("## Gerando extrato da conta 1 após transferência...")
conta_1.gerar_extrato()
