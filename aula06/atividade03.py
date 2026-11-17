for i in range (5):
    print(f'vendas {i + 1}')
    valor_final = float(input('\nDigite o valor: '))
    

    if valor_final >= 200:
        desconto = valor_final * 0.10
        print(f'\nValor: {desconto}')
        desconto = valor_final - desconto
        print(f'Valor final: {desconto}')

else:
    ('Sem desconto de 10%')
    
