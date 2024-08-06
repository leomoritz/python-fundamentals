# coding=utf-8
import time as timelib

"""
O módulo 'time' provê diversas funções relacionadas a tempo. Também pode ser útil conhecer os módulos datetime e calendar. 
Segue abaixo alguns exemplos de uso do módulo time.
"""
time = timelib.time()
print(f'O tempo atual local é: {timelib.ctime(time)}')

"""
A classe time.struct_time gera objetos sequenciais com valor de tempo retornado pelas funções gmtime() e localtime(). 
São objetos com interface de tupla nomeada: os valores podem ser acessados pelo índice e pelo nome do atributo.
"""
print('\nHORÁRIO GMT PADRÃO (UTC)')
gmtime = timelib.gmtime()
print('Tempo UTC: ' + str(gmtime))
print('Ano: ' + str(gmtime.tm_year))
print('Mês: ' + str(gmtime.tm_mon))
print('Dia: ' + str(gmtime.tm_mday))
print('Hora: ' + str(gmtime.tm_hour))
print('Minuto: ' + str(gmtime.tm_min))
print('Segundo: ' + str(gmtime.tm_sec))
print('Dia da semana: ' + str(gmtime.tm_wday))
print('Dia do ano: ' + str(gmtime.tm_yday))
print('Horário de verão: ' + str(gmtime.tm_isdst))

print('\nHORÁRIO LOCAL')
localtime = timelib.localtime()
print('Tempo local: ' + str(localtime))
print('Ano: ' + str(localtime.tm_year))
print('Mês: ' + str(localtime.tm_mon))
print('Dia: ' + str(localtime.tm_mday))
print('Hora: ' + str(localtime.tm_hour))
print('Minuto: ' + str(localtime.tm_min))
print('Segundo: ' + str(localtime.tm_sec))
print('Dia da semana: ' + str(localtime.tm_wday))
print('Dia do ano: ' + str(localtime.tm_yday))
print('Horário de verão: ' + str(localtime.tm_isdst))