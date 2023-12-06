import table_functions

texto = 'feliz natal'

secret = table_functions.converte_texto_matriz(texto)
print(secret)
secret = table_functions.jump_columns(secret)
print(secret)
secret = table_functions.jump_lines(secret)
print(secret)
matriz = [1,2,3,4,5]