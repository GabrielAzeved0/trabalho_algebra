import random
import numpy as np

def text_to_table(text):
    table = [char for char in text]
    table = [ord(char) for char in table]
    return table
    
def format_table(table):
    global ordem
    table = [table[i::ordem] for i in range(ordem)]
    return table

def table_order(table):
    global ordem
    ordem = len(table)**(1/2)
    while not ordem.is_integer():
        table.append(1)
        ordem = len(table)**(1/2)
    ordem = int(ordem)
    
def jump_columns(table):
    global ordem
    new_table = []
    jumps = random.randint(0, ordem-1)
    print(jumps)
    for line in table:
        new_line = []
        for x in range(ordem):    
            if (x+jumps) > (ordem-1):
                jump_aux = x + jumps - ordem
                new_line.append(line[jump_aux])
                continue            
            new_line.append(line[x+jumps]) 
        new_table.append(new_line)
    return new_table
    
def jump_lines():
    pass

def inverse_table(table):
    det = np.linalg.det(table)

    if det == 0:
        print("ERRO!! TENTE OUTRO TEXTO")
    else:
        nova_matriz = np.linalg.inv(table)
    return nova_matriz

def multiplie_table(table):
    
    n_random = random.randint(2, 10)
    nova_matriz = []

    for i in table:
        matriz = i * n_random
        nova_matriz.append(matriz)       
    return nova_matriz    

def increase_values(table):
    n_random = random.randint(2, 10)
    nova_matriz = []

    for i in table:
        matriz = i + n_random
        nova_matriz.append(matriz)       
    return nova_matriz  

def decrease_values(table):
    n_random = random.randint(2, 10)
    nova_matriz = []

    for i in table:
        matriz = i - n_random
        nova_matriz.append(matriz)       
    return nova_matriz 

