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
        print('')
        print('Você começa!')
        print('')
        while n != 0:
            m_retirado = usuario_escolhe_jogada(n, m)
            n = n - m_retirado
            print('Voce tirou',m_retirado,'peça(s).')
            if n == 0:
                print('Você ganhou!')
                return 'FIM' #conectar esse fim com placar e função campeonato
            else:          
                print('Agora restam', n, 'peça(s) no tabuleiro.')

            m_retirado = computador_escolhe_jogada(n,m)
            n = n - m_retirado
            print('O computador tirou',m_retirado,'peça(s).')
            if n == 0:
                print('O computador ganhou!')
                return 'FIM' #conectar esse fim com placar e função campeonato
            else:
                print('Agora restam', n, 'peça(s) no tabuleiro.')
       
    else:
        print('')
        print('Computador começa!')
        print('')
        while n != 0:
            m_retirado = computador_escolhe_jogada(n,m)
            n = n - m_retirado
            print('O computador tirou',m_retirado,'peça(s).')         
            if n == 0:
                print('O computador ganhou!')
                return 'FIM' #conectar esse fim com placar e função campeonato
            else:
                print('Agora restam', n, 'peça(s) no tabuleiro.')
            
            m_retirado = usuario_escolhe_jogada(n, m)
            n = n - m_retirado
            print('Voce tirou',m_retirado,'peça(s).')
            if n == 0:
                print('Você ganhou!')
                return 'FIM' #conectar esse fim com placar e função campeonato
            else:
                print('Agora restam', n, 'peça(s) no tabuleiro.')
