# A quantidade de notas pode ser ajustada conforme o desejado, mas altere a soma entre as notas e por quanto é dividido
n1 = float(input('Nota 1 '))
n2 = float(input('Nota 2 '))
n3 = float(input('Nota 3 '))
n4 = float(input('Nota 4 '))
m = (n1 + n2 + n3 + n4) / 4 # altere o numero 4 conforme quantas notas você adicionar

print('A média da sua nota é de {}'.format(m))
