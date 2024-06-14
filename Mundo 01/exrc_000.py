import random

array = []

numero = 0;
while numero < 4:
    numero += 1;
    array.append(input(f'Digite o {numero}° nome: '))

random = random.choice(array);
print(f'O nome escolhido foi {random}');