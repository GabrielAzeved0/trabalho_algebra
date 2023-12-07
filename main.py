import table_functions
import random

menu = """
-----------------------MENU-----------------------

1 - CRIPTOGRAFAR
2 - DESCRIPTOGRAFAR

Operação Desejada: 
"""
print(menu)
op = input()

if op == '1':
    tabela, segredo = table_functions.criptografa_texto()
    print(tabela, segredo)
if op == '2':
    pass



