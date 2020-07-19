def campeonato():
    
    op = int(input(''))
    
    placar_usuario = 0
    placar_computador = 0
        
    if op == 1 or op == 2:
        if op == 2:
            print('Voce escolheu um campeonato!')
            print('')
            
            while placar_computador < 3:
                
                print('**** Rodada', placar_computador + 1,' ****')
                print('')
                n = int(input('Quantas peças? '))
                m = int(input('Limite de peças por jogada? '))
                partida(n, m)
                placar_computador += 1

            print('Placar: Você',placar_usuario,'X',placar_computador,'Computador')  
            
        else:
            print('Voce escolheu uma partida isolada')
            print('')
            n = int(input('Quantas peças? '))
            m = int(input('Limite de peças por jogada? '))
            partida(n, m)
            placar_computador += 1
            print('')
            print('Placar: Você',placar_usuario,'X',placar_computador,'Computador')
            
    else:
        print('Opção inválida!!')
        campeonato()


print('Bem-vindo ao jogo do NIM! Escolha:')
print('')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato ',)
campeonato()
