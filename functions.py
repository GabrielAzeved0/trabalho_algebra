import random
import numpy as np

#FUNÇÕES PARA CRIPTOGRAFAR------------------------------------------------------------------------------------
def criptografa_texto():
    chave = ''
    texto = input()
    matriz = converte_texto_matriz(texto)
    for i in range(10):
        matriz, chave = sort_functions(matriz, chave)
    for linha in matriz:
        for i in range(len(linha)):
            linha[i] += 32
    return matriz, chave

def sort_functions(table, key):
    function_sorted = random.randint(1, 6)
    match function_sorted:
        case 1:
            table, key = jump_columns(table, key)
            return table, key
        case 2:
            table, key = jump_lines(table, key)
            return table, key
        case 3:
            #table, key = inverse_table(table, key)
            return table, key
        case 4:
            table, key = multiplie_table(table, key)
            return table, key
        case 5:
            table, key = increase_values(table, key)
            return table, key
        case 6:
            #table, key = decrease_values(table, key)
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

def imprime_texto_criptgrafado(table):
    texto_criptografado = ''
    for linha in table:
        for valor in linha:
            print(valor)
            print(chr(valor))
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
        new_table.append(table[x-jumps])
    return new_table, key

def inverse_table(table, key):
    code = '3'
    n_random = random.randint(0, 9)
    table = np.linalg.inv(table)
    key = key+code+str(n_random)
    return table, key

def multiplie_table(table, key):
    code = '4'
    global ordem
    n_random = random.randint(2, ordem-1)
    for linha in range(ordem):
        for coluna in range(ordem):
            table[linha][coluna] *= n_random      
    key = key+code+str(n_random)   
    return table, key

def increase_values(table, key):
    code = '5'
    global ordem
    n_random = random.randint(1, ordem-1)
    for linha in range(ordem):
        for coluna in range(ordem):
            table[linha][coluna] += n_random
    key = key+code+str(n_random)   
    return table, key  

def decrease_values(table, key):
    code = '6'
    global ordem
    n_random = random.randint(1, ordem-1)
    for linha in range(ordem):
        for coluna in range(ordem):
            table[linha][coluna] -= n_random
    key = key+code+str(n_random)    
    return table, key


#OPERAÇÕES PARA DESCRIPTOGRAFAR----------------------------------------------------------------------------------
