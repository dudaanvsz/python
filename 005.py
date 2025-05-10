#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
raio = float(input('Digite o número do raio: '))
volume = (4/3) * 3.1415 * raio ** 3
area = 4 * 3.1415 * raio ** 2

print(f'Volume da Esfera {volume}: ')
print(f'Area da Esfera {area}: ')
