p = float(input('Digite o valor do produto: '))
d = float(input('Digite o valor do desconto: ')) # se você quer um desconto com ',', no int coloque float
valorD = (p / 100) * d
ValorP = (p - valorD)


print('-' * 35) # efeito visual
print('O valor do produto com desconto é de: {:.2f}'.format(ValorP))
print('-' * 35) # efeito visual
