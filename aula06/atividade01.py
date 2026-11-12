ingresso = float(input('Valor do ingresso: '))

print('''
1 - INTEIRA (sem desconto)
2 - MEIA ENTRADA (50% de desconto)
3 - PROMOÇÃO (30% de desconto)
''')

desconto = 0

opcao = int(input('Informe a opção escolhida: '))

match opcao:
    case 1:
        print('Inteira')
        
    case 2:
        print('Meia entrada')
        desconto = ingresso * 0.50

    case 3:
        print('Promoção')
        desconto = ingresso * 0.30

    case _:
        print('Opção não registrada')

if opcao in [1, 2, 3]:
    valor_final = ingresso - desconto
    print(f'Valor do ingresso: R$ {ingresso} ')
    print(f'Desconto: R$ {desconto}')
    print(f'Total a pagar: R$ {valor_final}')

else:
    print('Escolha uma das opções acima.')





    


