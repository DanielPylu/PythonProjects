a = float(input('Digite a altura: '))
l = float(input('Digite a largura: '))
m = (a * l) / 2 # cada litro vai cubrir 2m², mas você pode deixar como você quiser


print('-' * 35) # efeito visual
print('São necessários {:.1f} Litros de tinta!'.format(m)) # se você quer um código preciso apaga o ":.1f" dentros dos {}

print('-' * 35) # efeito visual
