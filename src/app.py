import random
import time

acoes_possiveis = ['pedra', 'papel', 'tesoura']
vencedor = ''
pontuacao_usuario = 0
pontuacao_computador = 0
jogar_novamente = ''

while True:

    computador = random.choice(acoes_possiveis)

    # Escolha do usuário
    usuario = str(input('Escolha uma das opções - [pedra] || [papel] || [tesoura] || [s] = SAIR \n'
                        ''))

    if not usuario.isalpha() or usuario not in acoes_possiveis:
        print('Escolha uma opçõa válida \n')
        continue
    elif usuario == 's' or usuario == 'S':
        print('Saindo do jogo...')
        time.sleep(2)
        exit(0)

        # Game
    if usuario == computador:
        print(f'Você escolheu {usuario} e computador {computador}, EMPATE! \n')
    elif usuario == 'pedra':
        if computador == 'tesoura':
            print(f'Você escolheu PEDRA e o computador escolheu TESOURA \n')
            vencedor = usuario
            print(f'Você ganhou! PEDRA quebra TESOURA \n')
            pontuacao_usuario += 1
        else:
            vencedor = computador
            print(f'Você escolheu PEDRA e o computador escolheu PAPEL \n')
            pontuacao_computador += 1
            print(f'Você perdeu! PAPEL encobre PEDRA \n')

    elif usuario == 'papel':
        if computador == 'pedra':
            print(f'Você escolheu PAPEL e o computador escolheu PEDRA \n')
            vencedor = usuario
            print(f'Você ganhou! PAPEL encobre PEDRA \n')
            pontuacao_usuario += 1
        else:
            vencedor = computador
            print(f'Você escolheu PAPEL e o computador escolheu TESOURA \n')
            pontuacao_computador += 1
            print(f'Você perdeu! TESOURA corta PAPEL \n')

    elif usuario == 'tesoura':
        if computador == 'papel':
            print(f'Você escolheu TESOURA e o computador escolheu PAPEL \n')
            vencedor = usuario
            print(f'Você ganhou! TESOURA corta PAPEL \n')
            pontuacao_usuario += 1
        else:
            vencedor = computador
            print(f'Você escolheu TESOURA e o computador escolheu PEDRA \n')
            pontuacao_computador += 1
            print(f'Você perdeu! PEDRA quebra TESOURA \n')

    jogar_novamente = str(input('Deseja continuar? [s] = SIM | NÃO = Digite qualquer coisa para sair \n '))
    if jogar_novamente == 's' or jogar_novamente == 'S':
        continue
    else:
        print(f'Pontuação final computador = [{pontuacao_computador}] \n')
        print(f'Pontuação final usuário = [{pontuacao_usuario}] \n')
        exit(0)
