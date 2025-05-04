# Interação

def main():
    total = 0
    
    while True:
        try:
            qtd_bilhetes = int(input("Digite a quantidade de bilhetes que deseja comprar (1 a 5): "))
            if validar_qtd_bilhetes(qtd_bilhetes):
                break
            print("Quantidade inválida de bilhetes! Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

    i = 0
    while i < qtd_bilhetes:
        try:
            idade = int(input(f"Digite a idade do comprador {i + 1}: "))
            preco_ingresso = calcular_preco(idade)
            
            if preco_ingresso == -1:
                print("Idade inválida! Digite uma idade entre 0 e 130.")
                continue
                
            total += preco_ingresso
            i += 1
        except ValueError:
            print("Por favor, digite uma idade válida.")
    
    print(f"Valor total dos ingressos: R$ {total}")

if __name__ == "__main__":
    main()