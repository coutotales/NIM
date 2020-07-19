def usuario_escolhe_jogada(n, m):

    x = False

    while not x:
        m_retirado = int(input('Quantas peças você vai tirar? '))
        
        if m_retirado <= m and m_retirado > 0 and m_retirado <= n:
            x = True
            n = n - m_retirado
            #print('Voce tirou', m_retirado, 'peça(s).')
            #if n != 0:
                #print('Agora restam', n, 'peça(s) no tabuleiro.')
            #partida(n, m)
            
        else:
            print('')
            print('Oops! Jogada inválida! Tente de novo.')
            print('')
            
    return m_retirado
    #partida(n, m)
