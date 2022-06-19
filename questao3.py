import json

try:
    arquivo_json = open("dados.json")
except:
    print("Erro ao carregar o arquivo")
    exit()
try:
    dados = json.load(arquivo_json)
except:
    print("Erro ao carregar o arquivo json")
    exit()


def menor_faturamento(dados):
    menor_faturamento=""
    dia_do_menor_faturamento=""
    total_de_dias = len(dados)

    for i in range(total_de_dias):
        if(i==0):
            menor_faturamento = dados[i]['valor']
            dia_do_menor_faturamento=dados[i]['dia']
        else:
            # a condição dados[i]['valor'] > 0 é utilizada para evitar os dias em que não ocorreu faturamento 
            if dados[i]['valor']<menor_faturamento and dados[i]['valor'] > 0:
                menor_faturamento = dados[i]['valor']
                dia_do_menor_faturamento=dados[i]['dia']

    print(f"O menor faturamento foi de {menor_faturamento} e ocorreu no dia {dia_do_menor_faturamento}")
    

def maior_faturamento(dados):
    maior_faturamento=""
    dia_do_maior_faturamento=""
    total_de_dias = len(dados)
    for i in range(total_de_dias):
        if(i==0):
            maior_faturamento = dados[i]['valor']
            dia_do_maior_faturamento=dados[i]['dia']
        else:
             
            if dados[i]['valor']>maior_faturamento:
                maior_faturamento = dados[i]['valor']
                dia_do_maior_faturamento=dados[i]['dia']

    print(f"O maior faturamento foi de {maior_faturamento} e ocorreu no dia {dia_do_maior_faturamento}")

def media_mensal(dados):
    quantidade_de_dias_sem_faturamento=0
    valor_total=0
    total_de_dias = len(dados)
    for i in range(total_de_dias):
        if(dados[i]['valor']==0):
            quantidade_de_dias_sem_faturamento+=1
        else:
            valor_total+=dados[i]['valor']

    dias_com_faturamento = total_de_dias - quantidade_de_dias_sem_faturamento

    media = valor_total/dias_com_faturamento
    
    return media

def dias_com_faturamento_maior_que_a_media(dados):
    
    media_de_faturamento = media_mensal(dados)
    total_de_dias = len(dados)
    quantidade_acima_da_media=0

    for i in range(total_de_dias):
             
        if dados[i]['valor']>media_de_faturamento:
            quantidade_acima_da_media +=1
    
    print(f"{quantidade_acima_da_media} dias tiveram um faturamento superior a média mensal de {media_de_faturamento}")




menor_faturamento(dados)
maior_faturamento(dados)
dias_com_faturamento_maior_que_a_media(dados)