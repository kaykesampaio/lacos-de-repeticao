
maior = 0

menor = 0

for p in range(1,6):
    pesso = float(input('Peso da {}° pessoa: 👉 '.format(p))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = pesso
        if peso < menor:
            menor = peso

print('O maior peso lido foi de {}Kg'.format(maior))

print('o menor peso lido foi de {}Kg'.format(menor))






