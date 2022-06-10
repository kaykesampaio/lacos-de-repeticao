
núm = int(input('Digite um número'))

tot = 0

for c in range(1, núm,1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')












