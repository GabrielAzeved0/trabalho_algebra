#OPERAÇÕES PARA DESCRIPTOGRAFAR----------------------------------------------------------------------------------
texto = input()

def texto_para_matriz():
    texto = input('Insira o texto: ')
    chave = input('Insira a chave: ')
    matriz = converte_texto_matriz(texto)
    return matriz, chave

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

def descripto_jump_columns(code):
    pass

def descript_jump_lines(code):
    pass

