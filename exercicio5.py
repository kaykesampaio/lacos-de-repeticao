
print('+=+' * 25)

print('\n{:👇^40}'.format(' Digite alguns valores abaixo '))

soma = 0

cont = 0

for c in range(1,8):
    v = int(input('\nDigite o {}° valor 👉 '.format(c)))
    if v % 2 == 0:
        soma = soma + v
        cont = cont + 1
print('\nVocê informou {} números PARES e a soma foi: {}'.format(cont, soma))
    

print('\n{:👻^40}\n'.format(' fim '))

print('+=+' * 25)