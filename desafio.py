#Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário
s0 = float(input('Informe o valor de s0: '))
v0 = float(input('Informe o valor de v0: '))
a = float(input('Informe o valor de a: '))
t = float(input('Informe o valor de t: '))
soma = s0 + v0*t + (a*t ** 2/2)

print(f'A posição do objeto no tempo {t} é de {soma:.2f} (m)')