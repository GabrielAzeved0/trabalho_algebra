import random
import numpy as np

#FUNÇÕES PARA CRIPTOGRAFAR------------------------------------------------------------------------------------
def criptografa_texto():
    chave = ''
    texto = input()
    texto = texto.replace(' ', '_')
    matriz = converte_texto_matriz(texto)
    print(matriz)
    for i in range(4):
        matriz, chave = sort_functions(matriz, chave)
    for linha in matriz:
        for i in range(len(linha)):
            linha[i] += 32
    return matriz, chave

def sort_functions(table, key):
    function_sorted = random.randint(1, 4)
    match function_sorted:
        case 1:
            table, key = jump_columns(table, key)
            return table, key
        case 2:
            table, key = jump_lines(table, key)
            return table, key
        case 3:
            table, key = multiplie_table(table, key)
            return table, key
        case 4:
            table, key = increase_values(table, key)
            return table, key
            

def converte_texto_matriz(texto):
    global ordem
    matriz = text_to_table(texto)
    table_order(matriz)
    matriz = format_table(matriz)
    return matriz
    
def text_to_table(text):
    table = [char for char in text]
    table = [ord(char) for char in table]
    print(table)
    return table
    
def format_table(table):
    global ordem
    table = [table[i:i+ordem] for i in range(0, len(table), ordem)]
    return table

def table_order(table):
    global ordem
    ordem = len(table)**(1/2)
    while not ordem.is_integer():
        table.append(1)
        ordem = len(table)**(1/2)
    ordem = int(ordem)

def imprime_texto_criptgrafado(table):
    texto_criptografado = ''
    for linha in table:
        for valor in linha:
            texto_criptografado += chr(valor)
    print(texto_criptografado)


#OPERAÇÕES COM MATRIZES------------------------------------------------------------------------------------
def jump_columns(table, key):
    code = '1'
    global ordem
    new_table = []
    jumps = random.randint(1, ordem-1)
    key = key+code+str(jumps)
    for line in table:
        new_line = []
        for x in range(ordem):            
            new_line.append(line[x+jumps-ordem-1])
        new_table.append(new_line)
    return new_table, key
    
def jump_lines(table, key):
    code = '2'
    global ordem
    new_table = []
    jumps = random.randint(1, ordem-1)
    key = key+code+str(jumps)
    new_table = []
    for x in range(ordem):
        if x+jumps > ordem-1:
            new_table.append(table[x+jumps-ordem])
            continue
        new_table.append(table[x+jumps])
    return new_table, key

def multiplie_table(table, key):
    code = '3'
    global ordem
    n_random = random.randint(2, 4)
    for linha in range(ordem):
        for coluna in range(ordem):
            table[linha][coluna] *= n_random      
    key = key+code+str(n_random)   
    return table, key

def increase_values(table, key):
    code = '4'
    global ordem
    n_random = random.randint(1, ordem-1)
    for linha in range(ordem):
        for coluna in range(ordem):
            table[linha][coluna] += n_random
    key = key+code+str(n_random)   
    return table, key