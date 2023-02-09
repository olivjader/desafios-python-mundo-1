km = int(input('Qual a velocidade atual do carro? '))
multa = km - 80
if km <=80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Opa, você excedeu o limite de 70kh!')
    print('Sua multa será de R${},00'.format(multa * 7))