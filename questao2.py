

def pertence_a_seguencia_de_fibonacci(valor):
    valor_anterior=1
    valor_mais_antigo=1
    valor_atual=0
  

    while valor_atual<valor:
        valor_atual=valor_anterior+valor_mais_antigo
        valor_mais_antigo=valor_anterior
        valor_anterior=valor_atual

    if(valor==valor_atual):
        print("O número informado pertence a seguência de Fibonacci")
    else:
        print("O número informado não pertence a seguência de Fibonacci")


valor = 610

pertence_a_seguencia_de_fibonacci(valor)

valor2 = 611

pertence_a_seguencia_de_fibonacci(valor2)