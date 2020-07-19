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
                #print('O computador tirou', m_retirado, 'peça(s).')
                #if n != 0:
                    #print('Agora restam', n, 'peça(s) no tabuleiro.')
                #partida(n, m)
    return m_retirado
