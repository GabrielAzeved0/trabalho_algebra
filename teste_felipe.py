import table_functions

import numpy as np

def table_order(table):
    global ordem
    ordem = len(table)**(1/2)
    while not ordem.is_integer():
        table.append(1)
        ordem = len(table)**(1/2)
    ordem = int(ordem) 

def text_to_table(text):
    table = [char for char in text]
    table = [ord(char) for char in table]
    table_order(table)
    format_table(table)
    return table
    
def format_table(table):
    global ordem
    table = [table[i::ordem] for i in range(ordem)]
    print(table)
    return table

texto_usuario = 'felipe ta atrasado'
matriz = text_to_table(texto_usuario)

det = np.linalg.det(matriz)

if det == 0:
    print("ERRO!! TENTE OUTRO TEXTO")
else:
    A_inv = np.linalg.inv(matriz)
    print(A_inv)
