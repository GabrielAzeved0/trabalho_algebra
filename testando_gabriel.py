import table_functions

'matriz de str'
texto_usuario = 'felipe ta atrasado'

matriz = table_functions.text_to_table(texto_usuario)
table_functions.table_order(matriz)
matriz = table_functions.format_table(matriz)
print(matriz)
table_functions.jump_columns(matriz)


