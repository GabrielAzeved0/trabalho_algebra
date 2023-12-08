import functions
import descripto_functions
import os

menu = """
-----------------------MENU-----------------------
      CODIGO                        OPERAÇÃO

        1        --------------  CRIPTOGRAFAR
        2        -------------- DESCRIPTOGRAFAR
  QUALQUER TECLA --------------      SAIR

Código da operação desejada: """

while True:
    print(menu, end='')
    op = input()

    match op:
        case '1':
            tabela, segredo = functions.criptografa_texto()
            print(f'\nChave para Descriptografia: {segredo}')
            functions.imprime_texto_criptgrafado(tabela)
        case '2':
            tabela, segredo = descripto_functions.texto_para_matriz()
            descripto_functions.descriptografa_matriz(tabela, segredo)
        case _:
            break
