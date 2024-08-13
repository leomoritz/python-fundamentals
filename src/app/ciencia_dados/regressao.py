import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas

"""
KDD (Knowledge Discovery in Databases) é um processo, de várias etapas, não trivial, interativo e iterativo, 
para identificação de padrões compreensíveis, válidos, novos e potencialmente úteis a partir de grandes volumes de dados.

O processo de KDD é composto por várias etapas, que podem ser resumidas em: 
# pré-processamento: seleção, preparação e transformação dos dados; 
# mineração de dados: aplicação de algoritmos de aprendizado de máquina para identificar padrões;
# pós-processamento: interpretação e avaliação dos resultados obtidos para obtenção de conhecimento.
"""

############# Pré-processamento #############

# Coleta e Integração
arquivo = pandas.read_csv("dados_dengue.zip")

anos = arquivo[['ano']]
casos = arquivo[['casos']]

############# Mineração de Dados #############

regr = LinearRegression()
regr.fit(X=anos, y=casos) # Realiza o treinamento com base nos anos (x) e casos (y) como resultado

ano_futuro = pandas.DataFrame(np.array([[2018]]), columns=['ano']) # cria um dataframe com o ano de 2018
casos_2018 = regr.predict(ano_futuro).item() # Realiza a previsão de casos para 2018

print(f"Casos previstos para 2018: {int(casos_2018)}")

############# Pós-processamento #############
plt.scatter(anos, casos, color='black') # incluído os dados da série no gráfico com pontos pretos.
plt.scatter(ano_futuro, casos_2018, color='red') # incluído os dados previstos para 2018 no gráfico com pontos vermelhos.
plt.plot(anos, regr.predict(anos), color='blue', linewidth=3) # incluído a linha de regressão em azul no gráfico.

plt.xlabel('Anos') # incluído label para o rótulo do eixo x
plt.ylabel('Casos de dengue') # incluído uma label para o rótulo do eixo y
plt.xticks([2018]) # incluído o ano de 2018 no eixo x
plt.yticks([int(casos_2018)]) # incluído o número de casos previstos para 2018 no eixo y

plt.show()
