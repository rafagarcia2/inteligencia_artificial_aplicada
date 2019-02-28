# Genetic Algorithm Implementation in Python

import random
import math
# Geração aleatória de uma população de n cromossomos
population = random.sample(range(100), 100)

#print(population)

def fitness(number):
    '''
    Retorna o valor de uma equação do segundo grau.
    Forma: 2*x^2 + 34*x + 12
    '''
    #x1 = (-b+ pow(24, 2)) / (2.0*1)
    return 4*pow(number, 2) - 50 * number + 120


# [Adaptação] Verificar a função objetiva f(x) de cada cromossomo x
best_adapt = []
for i in population:
    adapt = fitness(i)
    if (adapt < 0 and adapt > -40):
        print(i)
        best_adapt.append(i)

# [População] Cria-se uma nova população pela repetição a seguir:
new_population = random.sample(range(100), 100)

