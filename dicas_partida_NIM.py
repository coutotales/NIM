$ > python3 jogo_nim.py

Bem-vindo ao jogo do NIM! Escolha: # é importante o jogo começar. Pode ser através de um print "Bem-vindo..."

1 - para jogar uma partida isolada # chama partida 1 vezes
2 - para jogar um campeonato 2 # funcao campeonato() chama partida 3 vezes e contabiliza no placar 

Voce escolheu um campeonato!

**** Rodada 1 ****

Quantas peças? 3 #entrada 'n' da função partida()
Limite de peças por jogada? 1 #entrada 'm' da função partida()
#com base em 'n' e 'm' a função partida decide quem começa e chama a outra função correspondente

Computador começa! #entra a função computador_escolhe_jogada()
#com base em 'n' e 'm', a função retorna o valor de retirada com base na estratégia vencedora

O computador tirou uma peça. #saída da função computador_escolhe_jogada()
Agora restam 2 peças no tabuleiro. #com base na saída, função partida() calcula novo 'n' e armazena e printa

Quantas peças você vai tirar? 2 #alternância. Após computador, entra função usuario_escolhe_jogada. INPUT

Oops! Jogada inválida! Tente de novo. #para o caso de valor fora do 'm', retorna mensagem e repete comando de INPUT
#p/ checar se o INPUT do usuário é válido, usar um while condição booleana que se repetirá até se tornar True
#pensar em todas as possibilidades de erros: negativos, letras, etc. TESTAR

Quantas peças você vai tirar? 1 #INPUT para usuario_escolhe_jogada()

Você tirou uma peça. #OUTPUT para usuario_escolhe_jogada()    
Agora resta apenas uma peça no tabuleiro. #função partida() calcula novo 'n' e armazena e printa

O computador tirou uma peça. #entra a função computador_escolhe_jogada()
#com base em 'n' e 'm', a função retorna o valor de retirada com base na estratégia vencedora

Fim do jogo! O computador ganhou! # condição para o fim: n == 0

**** Rodada 2 ****

Quantas peças? 3
Limite de peças por jogada? 2

Voce começa!

Quantas peças você vai tirar? 2 
Voce tirou 2 peças.
Agora resta apenas uma peça no tabuleiro.

O computador tirou uma peça.
Fim do jogo! O computador ganhou!

**** Rodada 3 ****

Quantas peças? 4
Limite de peças por jogada? 3

Voce começa!

Quantas peças você vai tirar? 2
Voce tirou 2 peças.
Agora restam 2 peças no tabuleiro.

O computador tirou 2 peças.
Fim do jogo! O computador ganhou!

**** Final do campeonato! ****

Placar: Você 0 X 3 Computador