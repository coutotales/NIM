
def usuario_escolhe_jogada(n, m):

    x = False

    while not x:
        m_retirado = int(input('Quantas peças você vai tirar? '))
        print('')

        if m_retirado <= m and m_retirado > 0:
            x = True
            m = m_retirado
            
        else:
            print('Oops! Jogada inválida! Tente de novo.')
            print('')
                    
