print('=-=' * 25)

n = int(input('Digite um numero para ver sua tabuada: ')) 

for c in range(1, 11,):
    print('{} x {:2} = {}'.format(n, c, n * c))

print()

print('=-=' * 25)
