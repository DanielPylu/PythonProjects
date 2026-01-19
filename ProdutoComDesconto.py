p = float(input('Digite o valor do produto: '))
d = float(input('Digite o valor do desconto: ')) # se você quer um desconto com ',', no int coloque float
valorD = (p / 100) * d # p / 100 = 50, 50 * 5 = 250 - valor do desconto
ValorP = (p - valorD) # sempre bote o maior valor primeiro para não dar negativo


print('-' * 35) # efeito visual
print('O valor do produto com desconto é de: {:.2f}'.format(ValorP))
print('-' * 35) # efeito visual
