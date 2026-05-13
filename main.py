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
