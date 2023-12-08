#OPERAÇÕES PARA DESCRIPTOGRAFAR----------------------------------------------------------------------------------
texto = input()

def texto_para_matriz():
    texto = input('Insira o texto: ')
    chave = input('Insira a chave: ')
    matriz = converte_texto_matriz(texto)
    chave = inverter_key(chave)
    return matriz, chave

def descriptografa_matriz(matriz, lista_chave):
    for codigo in lista_chave:
        op = codigo[0]
        fator = codigo[1]
        matriz = desfaz_op(matriz, op, fator)
    imprime_texto_descriptgrafado(matriz)

def desfaz_op(matriz, op, fator):
    match op:
        case 1:
            matriz = descripto_jump_columns(matriz, fator)
        case 2:
            matriz = descript_jump_lines(matriz, fator)
        case 3:
            matriz = descript_multiplie_table(matriz, fator)
        case 4:
            matriz = descript_increase(matriz, fator)

def imprime_texto_descriptgrafado(table):
    texto_descriptografado = ''
    for linha in table:
        for valor in linha:
            texto_descriptografado += chr(valor)
    print(texto_descriptografado)

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
    table = [table[i:i+ordem] for i in range(0, len(table), ordem)]
    return table

def table_order(table):
    global ordem
    ordem = len(table)**(1/2)
    while not ordem.is_integer():
        table.append(1)
        ordem = len(table)**(1/2)
    ordem = int(ordem)
    
def inverter_key(segredo):
    segredo_str = str(segredo)
    pares = [segredo_str[i:i+2] for i in range(0, len(segredo_str), 2)]
    pares_invertidos = pares[::-1]
    return pares_invertidos

def descripto_jump_columns(table, fator):
    global ordem
    new_table = []
    jumps = fator
    for line in table:
        new_line = []
        for x in range(ordem):            
            new_line.append(line[x-jumps])
        new_table.append(new_line)
    return new_table

def descript_jump_lines(table, fator):
    global ordem
    new_table = []
    jumps = fator
    new_table = []
    for x in range(ordem):
        if x+jumps > ordem:
            new_table.append(table[x+jumps])        
        new_table.append(table[x+jumps])
    return new_table

def descript_multiplie_table(tabela,fator):
    global ordem

    for linha in range(ordem):
        for coluna in range(ordem):
            tabela[linha][coluna] /= fator
    return tabela

def descript_increase(tabela,fator):
    global ordem

    for linha in range(ordem):
        for coluna in range(ordem):
            tabela[linha][coluna] -= fator
    return tabela
