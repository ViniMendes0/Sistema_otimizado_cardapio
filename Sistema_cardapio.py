def mensagem_de_boas_vindas():
    
    print("Bem-vindo ao restaurante!")
    print("Por favor, o que você vai querer hoje?\n")

cardapio_porcoes = {

    1: {"nome": "Fritas", "Preço": 25.00},
    2: {"nome": "Fritas com queijo", "Preço": 30.00},
    3: {"nome": "Pão de Alho(unidade)", "Preço": 10.00},
    4: {"nome": "Nuggets (5 unidades)", "Preço": 8.00},
    5: {"nome": "Pastelzinho (10 unidades)", "Preço": 10.00},
    6: {"nome": "Mandioca frita", "Preço": 28.00},
    7: {"nome": "Bolinho de bacalhau(11 unidades)", "Preço": 30.00},
    8: {"nome": "Bolinho de Aipim(14 unidades)", "Preço": 26.00},
    9: {"nome": "Camarão a Milanesa", "Preço": 100.00},
    10: {"nome": "Salgadinhos Mix(10 unidades)", "Preço": 10.00},
}

cardapio_almoco = {
    11: {"nome": "Milanesa", "Descrição": "Arroz, batata frita, feijão e purê", "Preço": 22.00},
    12: {"nome": "Strogonoff", "Descrição": "Arroz, batata frita e purê", "Preço": 22.00},
    13: {"nome": "Carne de sol", "Descrição": "Arroz tropeiro, vinagrete e fritas", "Preço": 25.00},
    14: {"nome": "Filé grelhado", "Descrição": "Arroz, legumes ao vapor e feijão", "Preço": 18.00},
    15: {"nome": "Bisteca", "Descrição": "Arroz, farofa, feijão, couve e salada", "Preço": 18.00},
    16: {"nome": "Linguiça Toscana", "Descrição": "Arroz, farofa, feijão e salada", "Preço": 25.00},
    17: {"nome": "Salada", "Descrição": "Tomate, salada, cenoura e brócolis", "Preço": 5.00},
    18: {"nome": "Virada Paulista", "Descrição": "Arroz, tutu de feijão, couve, bisteca, ovo e banana frita", "Preço": 26.00},
    19: {"nome": "Picadinho", "Descrição": "Arroz, feijão, picadinho de carne com batata e cenoura", "Preço": 27.00},
    20: {"nome": "Feijoada", "Descrição": "Arroz, feijão, linguiça, calabresa, bacon, carne seca, couve e farofa", "Preço": 30.00},
}

cardapio_bebidas = {
    21: {"nome": "Água mineral", "Descrição": "Com gás e sem gás", "Preço": 2.50},
    22: {"nome": "Suco em lata", "Descrição": "Manga, Pessêgo, limão e uva", "Preço": 7.00},
    23: {"nome": "Suco natural", "Descrição": "Laranja, maracujá e limão", "Preço": 5.00},
    24: {"nome": "Refrigerante", "Descrição": "Coca-cola, Pepsi, Fanta, Guaraná", "Preço": 4.00},
    25: {"nome": "Limonada Suíça", "Descrição": "Suco natural de limão com gelo e leite condensado", "Preço": 8.00},
    26: {"nome": "Cerveja 1L", "Descrição": "Skol, Brahma, Heineken, Corona", "Preço": 9.00},
    27: {"nome": "Caipirinha", "Descrição": "Limão e morango", "Preço": 10.00},
    28: {"nome": "Whisky", "Descrição": "Soda italiana com Vodka", "Preço": 16.00},
}

cardapio_sobremesas = {
    29: {"nome": "Pudim", "Descrição": "Leite Condensado", "Preço": 12.00},
    30: {"nome": "Torta Holandesa", "Descrição": "Sabor: Chocolate", "Preço": 10.00},
    31: {"nome": "Torta de Limão", "Preço": 10.00},
    32: {"nome": "Mousse", "Descrição": "Sabor: Maracujá", "Preço": 11.00},
    33: {"nome": "Sorvete", "Descrição": "Chocolate, limão, coco e morango", "Preço": 4.00},
    34: {"nome": "Cupcake", "Descrição": "Baunilha, café e brigadeiro (unidade)", "Preço": 9.00},
    35: {"nome": "Donut", "Descrição": "Chocolate, manteiga de amendoim e morango (unidade)", "Preço": 5.00},
    36: {"nome": "Fatias de bolo", "Descrição": "Baunilha e morango", "Preço": 7.00},
}

def exibir_cardapio(cardapio, categoria):
    print(f"\n--- {categoria} ---")
    for codigo, item in cardapio.items():
        item_nome = item.get('nome', '')
        print(f"{codigo}. {item_nome} - R${item['Preço']:.2f}")

def escolher_itens(cardapio):
    itens_escolhidos = []
    while True:
        try:
            opcoes = input("\nDigite os números dos itens que você deseja, separados por vírgula (ou 0 para voltar ao menu): ")
            if opcoes.strip() == "0":
                break
            opcoes = [int(opcao.strip()) for opcao in opcoes.split(",")]
            for opcao in opcoes:
                if opcao in cardapio:
                    item = cardapio[opcao]
                    item_nome = item.get('nome', '')
                    itens_escolhidos.append(item)
                    print(f"\nVocê escolheu: {item_nome} - R${item['Preço']:.2f}")
                else:
                    print(f"Opção {opcao} inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira números válidos.")
    return itens_escolhidos

def calcular_total(itens):
    total = sum(item['Preço'] for item in itens)
    return total

def exibir_resumo_pedido(itens):
    print("\nResumo do seu pedido:")
    for item in itens:
        item_nome = item.get('nome', '')
        print(f"{item_nome} - R${item['Preço']:.2f}")
    total = calcular_total(itens)
    print(f"\nTotal a ser pago: R${total:.2f}")
    return total

def escolher_metodo_pagamento():
    print("\nEscolha o método de pagamento:")
    print("1. Dinheiro")
    print("2. Cartão de Crédito")
    print("3. Cartão de Débito")
    print("4. Pix")
    
    while True:
        try:
            opcao = int(input("Digite o número da seu pedido: "))
            if opcao in [1, 2, 3, 4]:
                return opcao
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

def processar_pagamento(total, metodo):
    if metodo == 1:
        print("\nVocê escolheu pagar com Dinheiro.")
        print(f"Por favor, pague o valor total de R${total:.2f} no caixa.")
    elif metodo == 2:
        print("\nVocê escolheu pagar com Cartão de Crédito.")
        # Simular inserção de informações de cartão
        input("Digite o número do cartão: ")
        input("Digite a data de validade (MM/AA): ")
        input("Digite o código CVV: ")
        print("Processando pagamento...")
    elif metodo == 3:
        print("\nVocê escolheu pagar com Cartão de Débito.")
        # Simular inserção de informações de cartão
        input("Digite o número do cartão: ")
        input("Digite a data de validade (MM/AA): ")
        input("Digite o código CVV: ")
        print("Processando pagamento...")
    elif metodo == 4:
        print("\nVocê escolheu pagar com Pix.")
        # Simular processo de pagamento com Pix
        print("Por favor, use o aplicativo do seu banco para escanear o QR code e realizar o pagamento.")
        input("Pressione Enter após completar o pagamento com Pix.")
    print("Pagamento realizado com sucesso!\n")

def main():
    mensagem_de_boas_vindas()
    pedido = []

    while True:
        print("\nCategorias de Cardápio:")
        print("1. Porções")
        print("2. Almoço")
        print("3. Bebidas")
        print("4. Sobremesas")
        print("5. Finalizar Pedido")
        
        try:
            categoria = int(input("\nEscolha a categoria que você deseja ver (ou 5 para finalizar): "))
            if categoria == 1:
                exibir_cardapio(cardapio_porcoes, "Porções")
                itens_escolhidos = escolher_itens(cardapio_porcoes)
                pedido.extend(itens_escolhidos)
            elif categoria == 2:
                exibir_cardapio(cardapio_almoco, "Almoço")
                itens_escolhidos = escolher_itens(cardapio_almoco)
                pedido.extend(itens_escolhidos)
            elif categoria == 3:
                exibir_cardapio(cardapio_bebidas, "Bebidas")
                itens_escolhidos = escolher_itens(cardapio_bebidas)
                pedido.extend(itens_escolhidos)
            elif categoria == 4:
                exibir_cardapio(cardapio_sobremesas, "Sobremesas")
                itens_escolhidos = escolher_itens(cardapio_sobremesas)
                pedido.extend(itens_escolhidos)
            elif categoria == 5:
                if not pedido:
                    print("Você não escolheu nenhum item. Por favor, escolha algo antes de finalizar o pedido.")
                else:
                    total = exibir_resumo_pedido(pedido)
                    metodo_pagamento = escolher_metodo_pagamento()
                    processar_pagamento(total, metodo_pagamento)
                    break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
