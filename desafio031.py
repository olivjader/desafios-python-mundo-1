km = int(input('Qual a distância da viagem? '))
if km > 200:
    print('Olá, sua viagem de {}Km custará R${}'.format(km, km * 0.45))
else:
    print('Olá, sua viagem de {}Km custará R${}'.format(km, km * 0.50))
print('Tenha uma boa viagem!')
