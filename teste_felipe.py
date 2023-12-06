import table_functions
import random

table = [[1,2,3],[2,3,4]]
n_random = random.randint(2, 10)
nova_matriz = []

for i in table:
    matriz = i + n_random
    nova_matriz.append(matriz)

print(nova_matriz)
print(n_random)

# import random

# table = [[1,2,3],[2,3,4]]
# n_random = random.randint(2, 10)
# nova_matriz = []

# for sublista in table:
#     nova_sublista = [i + n_random for i in sublista]
#     nova_matriz.append(nova_sublista)

# print(nova_matriz)
# print(n_random)
