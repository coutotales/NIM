
def computador_escolhe_jogada(n, m):
    m_retirado = 0
    n_sobra = (n - m_retirado)

    while m_retirado <= m and n_sobra % (m + 1) != 0:
    
        n_sobra = (n - m_retirado)
    
        if n_sobra % (m + 1) != 0:
            m_retirado += 1
        
        else:
            return m_retirado

