import functions
import descripto_functions

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
        tabela, segredo = descripto_functions.texto_para_matriz()
        print(tabela)
        print(segredo)
    case _:
        pass



