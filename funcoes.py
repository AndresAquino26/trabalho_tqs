# Trabalho feito por Andres Aquino Ferreira da Silva - Matrícula: 202310310811
# Teste e Qualidade de Software

# Funções

def calcular_preco(idade):
    if idade < 0 or idade > 130:
        return -1
    if idade <= 12:
        return 10
    elif idade <= 59:
        return 30
    else:
        return 15

def validar_qtd_bilhetes(qtd):
    return 1 <= qtd <= 5