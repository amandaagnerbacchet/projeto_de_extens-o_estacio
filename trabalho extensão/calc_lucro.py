def calcular_preco_venda():
    # Solicita o custo de fabricação do produto
    custo_fabricacao = float(input("Digite o custo de fabricação do produto: R$ "))

    # Solicita a porcentagem de lucro desejada
    porcentagem_lucro = float(input("Digite a porcentagem de lucro desejada (ex: 20 para 20%): "))

    # Calcula o valor do lucro bruto
    valor_lucro_bruto = (porcentagem_lucro / 100) * custo_fabricacao

    # Calcula o preço de venda
    preco_venda = custo_fabricacao + valor_lucro_bruto

    # Exibe o preço de venda
    print(f"\nPara ter um lucro de {porcentagem_lucro}%, você deve vender o produto por: R$ {preco_venda:.2f}")

    # Solicita a faixa de comissão do vendedor
    porcentagem_comissao = float(input("Digite a porcentagem de comissão do vendedor (ex: 5 para 5%): "))

    # Calcula o valor da comissão do vendedor
    valor_comissao = (porcentagem_comissao / 100) * preco_venda

    # Calcula o lucro líquido após descontar a comissão do vendedor
    lucro_liquido = valor_lucro_bruto - valor_comissao

    # Exibe os resultados
    print(f"\nLucro bruto por venda: R$ {valor_lucro_bruto:.2f}")
    print(f"Comissão do vendedor: R$ {valor_comissao:.2f}")
    print(f"Lucro líquido após comissão: R$ {lucro_liquido:.2f}")

# Chama a função para executar o cálculo
calcular_preco_venda()
