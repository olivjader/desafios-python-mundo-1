n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
# Verificando quem é menor.
if n1<n2 and n1<n3:
    menor = n1
if n2<n3 and n2<n1:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
# Verificando quem é maior.
if n1>n2 and n1>n3:
    maior = n1
if n2>n3 and n2>n1:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
# Verificando se não foi digitado números iguais
if n1 == n2 or n2 == n3 or n1 == n3:
    print('Espertinho você hein, digitou algum número repetido!')
    print('Rode novamente o programa')
else:
    print('O menor número foi o {} e o maior foi o {}'.format(menor, maior))
