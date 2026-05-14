#Entrada
def sistema_vendas():
    # Variáveis para armazenar o resumo das vendas
    total_vendas = 0
    total_bruto = 0.0
    total_descontos = 0.0
    total_liquido = 0.0

    while True:
        print("\n=== SISTEMA DE VENDAS ===")
        print("1 - Registrar venda")
        print("2 - Ver resumo parcial")
        print("3 - Encerrar sistema")
        
        opcao = input("Escolha uma opção: ")
#Processamento        


        if opcao == '1':
            print("\n--- Registrar Venda ---")
            nome_produto = input("Nome do produto: ")
            valor_unitario = float(input("Valor unitário: R$ "))
            quantidade = int(input("Quantidade: "))
            desconto_percentual = float(input("Desconto aplicado (em %): "))

# Cálculos da venda
            valor_bruto = valor_unitario * quantidade
            valor_desconto = valor_bruto * (desconto_percentual / 100)
            valor_final = valor_bruto - valor_desconto

# Atualizando os totais
            total_vendas += 1
            total_bruto += valor_bruto
            total_descontos += valor_desconto
            total_liquido += valor_final          

            print(f"\nValor bruto da venda: R$ {valor_bruto:.2f}")
            print(f"Desconto aplicado: {desconto_percentual}%")
            print(f"Valor do desconto: R$ {valor_desconto:.2f}")
            print(f"Valor final da venda: R$ {valor_final:.2f}")
            print("Venda registrada com sucesso!")

        elif opcao == '2':
            print("\n=== RESUMO PARCIAL ===")
            print(f"Total de vendas realizadas: {total_vendas}")
            print(f"Total bruto vendido: R$ {total_bruto:.2f}")
            print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
            print(f"Total líquido vendido: R$ {total_liquido:.2f}")

        elif opcao == '3':
            print("\n=== RESUMO FINAL ===")
            print(f"Total de vendas realizadas: {total_vendas}")
            print(f"Total bruto vendido: R$ {total_bruto:.2f}")
            print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
            print(f"Total líquido vendido: R$ {total_liquido:.2f}")
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida! Tente novamente.")

#Saída

sistema_vendas()