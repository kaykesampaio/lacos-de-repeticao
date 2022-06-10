
somaid = 0

médiaid = 0

mih = 0

nomevelho = ''

totm20 = 

for pe in range(1, 5):
    print('----- {}° PESSOA -----'.format(pe))
    
    nome = str(input('Nome 👉 ')).strip()
    
    idade = int(input('Idade 👉 '))
    
    sexo = str(input('Sexo [M/F]👉 ')).strip()
    
    somaid = somaid + idade
    
    if pe == 1 and sexo in 'Mm':
        midhm = idade
        nomevelho =  nome
    
    if sexo in 'Mm' and idade > mih:
        mih = idade 
        nomevelho = nome 
    
    if sexo in 'Ff' and idade < 20:
        totm20 = totm20 + 1


médiaid = somaid / 4

print('\nA média de idade do grupo é de {} anos'.format(médiaid))

print('\nO homem mais VELHO tem {} anos e se chama {}.'.format(mih,nomevelho))

print('\nAo todo são {} melheres com menos de 20 anos'.format(totm20))

 
















