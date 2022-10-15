from random import randint

certo = True
continuar = True
acertou = 0
errou = 0

print('-------------------------------------------------')
print('-------------Benvindo à JTech Game---------------')
print('-------------------------------------------------')

while continuar:
    tentativas = 3
    while certo:
        sorteado = randint(0,9)

        for x in range(1, 4):
            tenta = int(input(f'Tente pela {x}º vez: '))
            if tenta not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
                print('Escolha apenas números de 0 à 9...')
                tentativas = 3
                x = 1
                break
            else:
                tentativas -= 1
                if tenta == sorteado:
                    print(f'Acertou na {x}º tentativa, o número sorteado foi {sorteado}')
                    acertou = acertou + 1
                    certo = False
                    break
                else:
                    certo = True
                    errou = errou + 1
                    print('Tente mais uma vez!')
        if tentativas == 0 and sorteado != tenta:
            print(f'Acabaram as tuas tentativas, o número sorteado foi {sorteado}!')
            break

    cont = input('Quer continuar? Responda, Sim ou Não!')
    print('-------------------------------------------------')
    if cont in ['sim', 'Sim', 's']:
        continuar = True
        certo = True
        print('Obrigado por jogar com a JTech')
        print('-------------------------------------------------')

    elif cont in ['não', 'nao', 'Não', 'Nao', 'n']:
        print('Obrigado port ter participado no JTech Game!')
        if acertou > 1:
            print(f'Acertou {acertou} vezes!')
        else:
            print(f'Acertou {acertou} vez!')
        if errou > 1:
            print(f'Errou {errou} vezes!')
        else:
            print(f'Errou {errou} vez!')
        print('-------------------------------------------------')
        continuar = False
        break

    else:
        print('Escolha entre sim ou não!')