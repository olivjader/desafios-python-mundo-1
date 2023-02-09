from math import radians, sin, cos, tan
an = float(input('Digite um ângulo: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O ângulo de {:.1f} tem o seno de {:.2f}'.format(an, sen))
print('O ângulo de {:.1f} tem o cosseno de {:.2f}'.format(an, cos))
print('O ângulo de {:.1f} tem a tangente de {:.2f}'.format(an, tan))