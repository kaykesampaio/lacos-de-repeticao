
# Palíndromo é uma frase que dá para ler de traz para frente 

print('<<<<' * 25)

frase = str(input('Digite uma frase 👉 ')).strip().upper()

palavra = frase.split()

junto = ''.join(palavra)

inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]

print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('\nA frase digitada não forma um Palíndromo!')

print('>>>>' * 25)












