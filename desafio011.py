print('Digite a altura e a largura em metros, de uma parede para saber sua área e quantas latas de tinta irá isar')
a = float(input('Digite a altura '))
l = float(input('Digite a largura '))
A = a * l
print('Sua parede tem {:.2f} metros quadrados'.format(A))
print('Cada lata de tinta preenche 2m²')
lt = A / 2
print('Você irá precisar de {} latas de tinta'.format(lt))
