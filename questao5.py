def inverte_string(palavra):
    palavra_invertida=[]

    for i in range(len(palavra)-1,-1,-1):
        palavra_invertida.append(palavra[i])

    palavra_invertida = "".join(palavra_invertida)

    print(f' O inverso de {palavra} é {palavra_invertida}')

palavra = "processo"

inverte_string(palavra)