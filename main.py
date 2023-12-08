import functions
import descripto_functions

menu = """
-----------------------MENU-----------------------

1 - CRIPTOGRAFAR
2 - DESCRIPTOGRAFAR

Operação Desejada: 
"""
print(menu)

while True:
    op = input()

    match op:
        case '1':
            tabela, segredo = functions.criptografa_texto()
            print(tabela, segredo)
            functions.imprime_texto_criptgrafado(tabela)
        case '2':
            tabela, segredo = descripto_functions.texto_para_matriz()
            descripto_functions.descriptografa_matriz(tabela, segredo)
            
        case _:
            break
