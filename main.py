import functions
import random
import functions

menu = """
-----------------------MENU-----------------------

1 - CRIPTOGRAFAR
2 - DESCRIPTOGRAFAR

Operação Desejada: 
"""
print(menu)
op = input()

match op:
    case '1':
        tabela, segredo = functions.criptografa_texto()
        print(tabela, segredo)
        functions.imprime_texto_criptgrafado(tabela)
    case '2':
        pass
    case _:
        pass



