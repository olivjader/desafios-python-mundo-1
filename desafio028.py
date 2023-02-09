from random import randint
from time import sleep
computador = randint(0, 5)
print('-=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 20)
jogador = int(input('Em que número eu pensei? '))
print('POCESSANDO...')
sleep(2)
if computador == jogador:
    print('Você acertou!, pensei mesmo no {}'.format(jogador))
else:
    print('Você errou! Eu pensei no {}'.format(computador))
print('Tente novamente!')