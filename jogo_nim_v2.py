def computador_escolhe_jogada(n, m):
    m_retirado = 0
    n_sobra = (n - m_retirado)

    if n_sobra % (m + 1) == 0:
        m_retirado = m
        
    else:
        while m_retirado <= m and n_sobra % (m + 1) != 0:
            n_sobra = (n - m_retirado)
    
            if n_sobra % (m + 1) != 0:
                m_retirado += 1       
            else:
                n = n_sobra
               
    return m_retirado
    
def usuario_escolhe_jogada(n, m):
    x = False

    while not x:
        m_retirado = int(input('Quantas peças você vai tirar? '))
        
        if m_retirado <= m and m_retirado > 0 and m_retirado <= n:
            x = True
            n = n - m_retirado
                       
        else:
            print('')
            print('Oops! Jogada inválida! Tente de novo.')
            print('')
            
    return m_retirado

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if n % (m + 1) == 0:
        print('Você começa!')
        print()
        while n != 0:
            m_retirado = usuario_escolhe_jogada(n, m)
            n = n - m_retirado
            print('Voce tirou',m_retirado,'peça(s).')
            if n == 0:
                print()
                print('Você ganhou!')
                print()
                return 
            else:
                print()
                print('Agora restam', n, 'peça(s) no tabuleiro.')
                print()

            m_retirado = computador_escolhe_jogada(n,m)
            n = n - m_retirado
            print()
            print('O computador tirou',m_retirado,'peça(s).')
            print()
            if n == 0:
                print()
                print('O computador ganhou!')
                print()
                return
            else:
                print()
                print('Agora restam', n, 'peça(s) no tabuleiro.')
                print()
       
    else:
        print()
        print('Computador começa!')
        print()
        while n != 0:
            m_retirado = computador_escolhe_jogada(n,m)
            n = n - m_retirado
            print()
            print('O computador tirou',m_retirado,'peça(s).')
            print()
            if n == 0:
                print()
                print('O computador ganhou!')
                print()
                return 
            else:
                print()
                print('Agora restam', n, 'peça(s) no tabuleiro.')
                print()
            
            m_retirado = usuario_escolhe_jogada(n, m)
            n = n - m_retirado
            print()
            print('Voce tirou',m_retirado,'peça(s).')
            print()
            if n == 0:
                print()
                print('Você ganhou!')
                print()
                return 
            else:
                print()
                print('Agora restam', n, 'peça(s) no tabuleiro.')
                print()


def campeonato():
    
    op = int(input(''))
    
    placar_usuario = 0
    placar_computador = 0
        
    if op == 1 or op == 2:
        if op == 2:
            print()
            print('Voce escolheu um campeonato!')
            print('')
            
            while placar_computador < 3:
                print()
                print('**** Rodada', placar_computador + 1,'****')
                print('')
                partida()
                placar_computador += 1
            print()
            print('**** Final do campeonato! ****')
            print('')
            print('Placar: Você',placar_usuario,'X',placar_computador,'Computador')  
            
        else:
            print()
            print('Voce escolheu uma partida isolada')
            print('')
            partida()
            placar_computador += 1
            print('')
            print('Placar: Você',placar_usuario,'X',placar_computador,'Computador')
            print()
    else:
        print()
        print('Opção inválida!!')
        print()
        campeonato()


print('Bem-vindo ao jogo do NIM! Escolha:')
print('')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato ',)
campeonato()

