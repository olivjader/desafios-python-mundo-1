p = float(input('Digite o valor de um produto para saber o valor com desconto de 5% '))
d = p * (5/100)
pf = p - d
print('O valor final com desconto ficou R${:.2f}'.format(pf))
