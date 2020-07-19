def computador_escolhe_jogada(n, m):
    m_retirado = 0
    n_sobra = (n - m_retirado)

    while m_retirado <= m and n_sobra % (m + 1) != 0:
    
        n_sobra = (n - m_retirado)
    
        if n_sobra % (m + 1) != 0:
            m_retirado += 1
        
        else:
            n = n_sobra
            print('O computador tirou', m_retirado, 'peça(s).')
            if n != 0:
                print('Agora restam', n, 'peça(s) no tabuleiro.')
            partida(n, m)

def usuario_escolhe_jogada(n, m):

    x = False

    while not x:
        m_retirado = int(input('Quantas peças você vai tirar? '))
        
        if m_retirado <= m and m_retirado > 0:
            x = True
            n = n - m_retirado
            print('Voce tirou', m_retirado, 'peça(s).')
            if n != 0:
                print('Agora restam', n, 'peça(s) no tabuleiro.')
            partida(n, m)
            
        else:
            print('')
            print('Oops! Jogada inválida! Tente de novo.')
            print('')

def partida(n, m):

    while n != 0:
                
        if n % (m + 1) != 0:
            print('')
            print('Computador joga!')
            print('')
              
            return computador_escolhe_jogada(n, m)
                        
        else:
            print('')
            print('Você joga!')
            print('')
            
            return usuario_escolhe_jogada(n, m)
               
    print('Fim do jogo! O computador ganhou!')  

n = int(input('Quantas peças? '))
m = int(input('Limite de peças por jogada? '))
partida(n, m)
