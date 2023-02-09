s = float(input('Digite o salário do empregado para saber seu novo salário com aumento e 15% '))
a = s * (15/100)
sf = s + a
print('O salário com aumento de 15% ficou em R${:.2f}'.format(sf))
