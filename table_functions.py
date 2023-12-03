import random

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

def inverse_table():
    pass

def multiplie_table(): 
    pass

def increase_values():
    pass

def decrease_values():
    pass
