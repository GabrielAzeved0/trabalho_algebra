#OPERAÇÕES PARA DESCRIPTOGRAFAR----------------------------------------------------------------------------------
texto = input()

def texto_para_matriz():
    texto = input('Insira o texto: ')
    chave = input('Insira a chave: ')
    matriz = converte_texto_matriz(texto)
    print(matriz)
    chave = inverter_key(chave)
    return matriz, chave

def descriptografa_matriz(matriz, lista_chave):
    for codigo in lista_chave:
        op = codigo[0]
        fator = int(codigo[1])
        print(op, fator)
        matriz = desfaz_op(matriz, op, fator)
        print(matriz)
    imprime_texto_descriptgrafado(matriz)

def desfaz_op(matriz, op, fator):
    match op:
        case '1':
            matriz = descripto_jump_columns(matriz, fator)
            return matriz
        case '2':
            matriz = descript_jump_lines(matriz, fator)
            return matriz
        case '3':
            matriz = descript_multiplie_table(matriz, fator)
            return matriz
        case '4':
            matriz = descript_increase(matriz, fator)
            return matriz

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
        table.append(32)
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
    for linha in table:
        nova_linha = linha[jumps:] + linha[:jumps]
        new_table.append(nova_linha)
    print('ok1')
    return new_table

def descript_jump_lines(table, fator):
    global ordem
    new_table = []
    jumps = fator
    new_table = []
    new_table = table[jumps:] + table[:jumps]
    print('ok2')
    return new_table

def descript_multiplie_table(tabela,fator):
    global ordem

    for linha in range(ordem):
        for coluna in range(ordem):
            tabela[linha][coluna] /= fator
            tabela[linha][coluna] = int(tabela[linha][coluna])
    print('ok3')
    return tabela

def descript_increase(tabela,fator):
    global ordem

    for linha in range(ordem):
        for coluna in range(ordem):
            tabela[linha][coluna] -= fator
    print('ok4')
    return tabela
