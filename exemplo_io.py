import datetime

# Este é o meu primeiro programa
print("Hello World")
nome = input("Entre com seu nome: ")
print(f"Iremos calcular o IMC de {nome}")
peso = eval(input("Informe seu peso: "))
altura = eval(input("Informe sua altura: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é de {imc:.2f}")

"""
Abaixo está uma forma de como formatar e concatenar a apresentação de valores numéricos com strings.
"""
hora = datetime.datetime.now().hour
minuto = datetime.datetime.now().minute
segundos = datetime.datetime.now().second
print("O cálculo do IMC foi finalizado às " + str(hora) + " : " + str(minuto) + " : " + str(segundos))
print("O cálculo do IMC foi finalizado às {} : {} : {}".format(hora, minuto, segundos))
print(f"O cálculo do IMC foi finalizado às {hora} : {minuto} : {segundos}")




