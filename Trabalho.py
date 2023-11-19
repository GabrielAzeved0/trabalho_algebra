
def menu():
    print("1 - CODIFICAR UMA MENSAGEM")
    print("2 - DECODIFICAR UMA MENSAGEM")
    
    return int(input("DIGITE SUA OPÇÃO: "))

substituicao = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
        't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ':27}

def codificar():
    
    while True:
        chave = int(input("\nCrie uma chave de 4 digitos: "))
        chave_codificar = list(chave)
        det = (chave_codificar[0] * chave_codificar[3]) - (chave_codificar[1] * chave_codificar[2])
    
        if det == 0:
            print("\nEssa chave não poderá ser aceita!")
    mensagem = input("\nDigite a frase que deseja codificar: ")
    
    #VERIFICANDO SE PRECISARÁ REPETIR A ULTIMA LETRA
    if len(mensagem) % 2 != 0:
        mensagem = mensagem + mensagem[-1]
        
    #retirar acentos    
    
    
    #trocando as letras da mensagem por numeros       
    letra_por_numero = ''.join(str(substituicao[c] for c in mensagem))
    
    #criptografando as letras
    criptografando = []
    for i in range(0, len(letra_por_numero), 2):
        if i+1 < len(letra_por_numero):
            valor1 = letra_por_numero[i] * chave_codificar[0] + letra_por_numero[i+1] * chave_codificar[1]
            if valor1 > 27:
                valor1 = valor1 % 27
                criptografando.append(valor1)
            else:    
                criptografando.append(valor1)
            valor2 = letra_por_numero[i] * chave_codificar[2] + letra_por_numero[i+1] * chave_codificar[3]
            if valor1 > 27:
                valor2 = valor2 % 27
                criptografando.append(valor2)
            else:    
                criptografando.append(valor2)
                  
    mensagem_criptografada = ''.join(str(substituicao[c] for c in criptografando))        
