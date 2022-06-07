print('👻' * 25)

p = int(input('\nPrimeiro termo 👉 ')) #primeiro

r = int(input('Razão 👉 ')) # razão

d = p + (10 - 1) * r # Décimo

for c in range(p, d + r, r):
    print('{} '.format(c), end='👉 ')
print(' ACABOU.')

print('👻' * 25)

