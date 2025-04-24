from math import sqrt

a = int(input('Digite o valor do A: '))
b = int(input('Digite o valor do B: '))
c = int(input('Digite o valor do C: '))

delta = b**2 - 4*a*c
raiz_1 = (-b + sqrt(delta))/2*a
raiz_2 = (-b - sqrt(delta))/2*a

print(f'As raizes são: {raiz_1} e {raiz_2}')
