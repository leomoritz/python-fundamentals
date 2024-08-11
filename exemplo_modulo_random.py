import random as rndm

# FUNÇÕES PARA NÚMEROS REAIS

# Número de ponto flutuante no intervalo [0.0, 1.0)
print(rndm.random())

# Número de ponto flutuante N tal que a ≤ N ≤ b
print(rndm.uniform(4, 10))

# Distribuição gaussiana. mu é a média e sigma é o desvio padrão.
print(rndm.gauss(10, 5))

# Distribuição normal. mu é a média e sigma é o desvio padrão.
print(rndm.normalvariate(10, 5))

# FUNÇÕES PARA NÚMEROS INTEIROS

# Um elemento selecionado aleatório de range(start, stop, step), mas sem construir um objeto range.
print(rndm.randrange(50))
print(rndm.randrange(1, 100))
print(rndm.randrange(10, 30, 5))

# Número inteiro N tal que a ≤ N ≤ b
print(rndm.randint(5, 20))

# FUNÇÕES PARA SEQUÊNCIAS

# Elemento aleatório de uma sequência não vazia seq.
seqNonEmpty = [10, 20, 30]
print(rndm.choice(seqNonEmpty))

# Embaralha a sequência x no lugar.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rndm.shuffle(x))

# Uma sequência de tamanho k de elementos escolhidos da população pop, sem repetição. Usada para amostragem sem substituição.
pop = [10, 20, 30]
k = 2
print(rndm.sample(pop, k))