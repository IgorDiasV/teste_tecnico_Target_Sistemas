def percentual_de_representacao_de_cada_estado(dados):
    quantidade_de_estados = len(dados)
    faturamento_total=0

    for i in range(quantidade_de_estados):
        faturamento_total+=dados[i]['valor']
    
    for i in range(quantidade_de_estados):
        
        percentual_do_estado =  (dados[i]['valor']/faturamento_total)*100
        
        # o percentual está sendo convertido para int para mostrar apenas os digitos mais representativos.
        print(f"o estado {dados[i]['estado']} teve {int(percentual_do_estado)}% de contribuição no faturamento mensal")


dados = [{"estado":"SP","valor":67836.43},{"estado":"RJ","valor":36678.66},
        {"estado":"MG","valor":29229.88},{"estado":"ES","valor":27165.48},
        {"estado":"Outros","valor":19849.53}]

percentual_de_representacao_de_cada_estado(dados)