par = []
impar = []
for c in range(1, 6):
    num = int(input('Digite um numero: '))
    if (num % 2) == 0:
        par.append(num)
    else:
        impar.append(num)

print(f' Os numeros pares são {par} e os numeros impares são {impar}')
