import random




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

def table_order(table):
    global ordem
    ordem = len(table)**(1/2)
    while not ordem.is_integer():
        table.append(1)
        ordem = len(table)**(1/2)
    ordem = int(ordem)
    pass
    
def jump_columns(table):
    global ordem
    new_table = []

    for lines in range(ordem):
        new_table.append([])
    for line in table:
        for column in table:
            line.append(table[])
    
    jumps = random.randint(0, ordem)
    print(jumps)

def jump_lines():
    pass

def inverse_table():
    pass

def multiplie_table():
    pass

def increase_values():
    pass

def decrease_values():
    pass
