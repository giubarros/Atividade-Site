x = 1
y = []

while x <= 6:
    numero = int(input('Digite um número:'))
    y.append(numero)
    x += 1
print(f'o maior valor é {max(y)}')
print(f'o menor valor é {min(y)}')
print(f'A media é:  {sum(y)/5} ')
