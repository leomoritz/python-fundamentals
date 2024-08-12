idadeCrianca = eval(input("Informe a idade da criança: "));

if idadeCrianca < 5:
    print("A criança deve ser vacinada contra a gripe.")
    print("Procure o posto de saúde mais próximo.")
elif idadeCrianca == 5:
    print("A vacina estará disponível em breve.")
    print("Aguarde as próximas informações.")
else:
    print("A vacinação só ocorrerá daqui a 3 meses.")
    print("Informe-se novamente neste prazo.")

print("Cuida da saúde sempre. Até a próxima!")