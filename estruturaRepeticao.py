# Estrutura FOR
for item in range(2, 9, 3):
    print(item)
print("Contagem do range foi finalizada!")

nome = input("Informe seu nome: ")

for letra in nome:
    print(letra)
print("Nome soletrado com sucesso!")

print("Segue abaixo os nomes dos membros da família Rosa:")
nomes = ['Leônidas', 'Bruna', 'Hanna']

for nome in nomes:
    print(nome)
print("Essa é uma família onde a base é Cristo!")

# Estrutura WHILE
palavra = input("Entre com qualquer palavra: ")

while palavra != "sair":
    print(f"A palavra digitada foi {palavra.upper()}")
    palavra = input("Digite sair para encerrar o laço: ")
print("Você digitou sair e agora está fora do laço.")

"""
O bloco do-while não existe em Python, porém podem ser criadas adaptações com os recursos existentes na linguagem.
Para casos onde se deseja utilizar um loop infinito, basta utilizar a estrutura abaixo:
while true:
    print("Coloque aqui dentro a(s) instrução(ões) que deseja repetir infinitamente")
"""

# Usando a instrução break para forçar a interrupção do laço
while True:
    print('Você está no primeiro laço.')
    opcao1 = input('Deseja sair dele? Digite SIM para isso. ')
    if opcao1 == 'SIM':
        break  # este break é do primeiro laço
    else:
        while True:
            print('Você está no segundo laço.')
            opcao2 = input('Deseja sair dele? Digite SIM para isso. ')
            if opcao2 == 'SIM':
                break  # este break é do segundo laço
            print('Você saiu do segundo laço.')
print('Você saiu do primeiro laço')

# Usando a instrução continue para interromper apenas a repetição corrente e ir para o próximo item da iteração
for num in range(1,11):
    if num == 5:
        print("Vou encerrar por aqui e ir para a próxima iteração do laço")
        continue
    else:
        print(num)
print("Laço encerrado")

# Usando a instrução pass para ignorar a execução de uma condição verdadeira e ir para a próxima iteração
for num in range(1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado')
