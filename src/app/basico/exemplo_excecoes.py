import math

# Captura de exceção genérica
try:
    num = eval(input("Entre com um número inteiro: "))
    print(num)
except:
    print("É necessário informar um número inteiro!")

# Captura de exceção de determinado tipo
try:
    num = eval(input("Entre com um número inteiro: "))
    print(num)
except NameError:
    print("É necessário informar um número inteiro!")

# Captura de exceção de múltiplos tipos
try:
    num = eval(input("Entre com um número inteiro: "))
    print(num)
except ValueError:
    print("Mensagem de erro para ValueError")
except IndexError:
    print("Mensagem de erro para IndexError")
except:
    print("Mensagem de erro para qualquer outra exceção")

# O tratamento completo das exceções
try:
    num = eval(input("Entre com um número inteiro: "))
except:
    print("É necessário informar um número inteiro!")
else:
    print(f"A raiz quadrada de {num} é {math.sqrt(num)}")
finally:
    print("Independentemente se deu certo ou não, este bloco será executado")

"""
O tratamento de eventos é similar ao tratamento de exceções. Assim como podemos tratar as exceções ocorridas em tempo de execução, 
podemos tratar os eventos criados por ações externas, como interações de usuário realizadas por meio de uma interface gráfica de usuário (GUI).
Um evento é a notificação de que alguma coisa aconteceu, como um clique de mouse sobre um elemento botão. 
O tratador do evento é o segmento de código que será executado em resposta à ocorrência do evento.
"""
