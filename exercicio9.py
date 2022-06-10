
# mostrador de idade

from datetime import date

atual = date.today().year

nasc = int(input('Em que ano a pessoa nasceu? 👉 '))

idade = atual - nasc

print('Essa pessoa tem {} anos'.format(idade))






