import table_functions
import random

table = [1,2,3]
n_random = random.randint(2, 10)
nova_matriz = []

for i in table:
    matriz = i * n_random
    nova_matriz.append(matriz)

print(nova_matriz)
print(n_random)