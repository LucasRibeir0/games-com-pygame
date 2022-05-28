import time

import pygame,random
#Mensagem para exibir informações sobre o desenvolvedor do jogo no terminal
desenvolvedor = {'Desenvolvedor: ':'Lucas Ribeiro Goncalves'}
for k,v in desenvolvedor.items():
    nomedev = (f'{k} {v}')

#Carregando as imagens que serão usadas no game
personagem = pygame.image.load("imagens/avatar.png")
cenario = pygame.image.load("imagens/cenario1.png")
coracao = pygame.image.load("imagens/coracao.png")
coracaoq = pygame.image.load("imagens/coracao-q.png")
coracaov = pygame.image.load("imagens/coracao-v.png")
cenario_intro = pygame.image.load("imagens/cenario-intro.png")

#Pegando largura e altura dos objetos criados
largura_da_janela = cenario.get_width()
altura_da_janela = cenario.get_height()
largura_do_personagem = personagem.get_width()
altura_do_personagem = personagem.get_height()
largura_do_coracao = coracao.get_width()
altura_do_coracao = coracao.get_height()
largura_do_coracao_q = coracaoq.get_width()
altura_do_coracao_q = coracaoq.get_height()
largura_do_coracao_v = coracaov.get_width()
altura_do_coracao_v = coracaov.get_height()

#Criando outras variáveis
FPS = 35
velocidade = 8
iteracao = 35
iteracao1 = 40
iteracao2 = 500
vidas = 5
start = '-Pressione Enter para jogar'
nome_jogo = 'Game Love'
config = '-Pressione "C" para Configurações'
pts = 'Pontuação: '
vds = 'Vidas: '
msg1_gameover = 'Continuar'
msg2_gameover = 'Sair'
pos_texto_dev = ((largura_da_janela/3.5),20)
pos_texto_titulo = ((largura_da_janela/2.7),(altura_da_janela/2.4))
pos_texto_start = ((largura_da_janela/3),(altura_da_janela/1.9))
pos_pts = (10, 0)
pos_vds = (10,25)
pos1_gameover = ((largura_da_janela/3.5),(altura_da_janela/1.5))
pos2_gameover = ((largura_da_janela/1.76),(altura_da_janela/1.5))
pos_texto_config = ((290,altura_da_janela-70))
contador = contador1 = contador2 = vez = recorde = 0
lista_coracao = []
lista_coracao_q = []
lista_coracao_v = []
janela_aberta = True
vermelho = (139,0,0)
laranja = (255,69,0)
rosa = (255,20,147)
preto = (28,28,28)
verde = (0,255,0)
branco = (255,255,255)
chocolate = (210,105,30)
musica_na_tela = 50
pedido = {'nome':'"O coracao','pedido':'tem razoes que a propria razao desconhece".'}
teclas = {'direita':False,'esquerda':False}
musica = False



def MoverJogador(jogador,teclas,dimensoes):
    # Função do movimento do avatar
    borda_esquerda = 0
    borda_direita = dimensoes[0]
    if teclas['esquerda'] and jogador['objRect'].left > borda_esquerda:
        jogador['objRect'].x -= jogador['velocidade']
    if teclas['direita'] and jogador['objRect'].right < borda_direita:
        jogador['objRect'].x += jogador['velocidade']
def MoverCoracao(coracao):
    # Faz o coração se movimentar
    coracao['objRect'].y += coracao['velocidade']
def CriaObjetos(lista_objeto,largura_objeto,altura_objeto,img_objeto, largura_janela):
    #Construindo os corações e colocando na lista
        posx = random.randint(0, largura_janela-largura_objeto)
        posy = -altura_objeto
        vel_random = random.randint(3,8)
        #Colocando os objetos na lista
        lista_objeto.append({'objRect':pygame.Rect(posx,posy,largura_objeto,altura_objeto),'imagem':img_objeto,'velocidade':vel_random})
        
        
def configuracoes():
    conf = True
    while conf:
        cenario_config = pygame.image.load("imagens/cenario-config.png")
        janela.blit(cenario_config,(0,0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # Se pressionar 'v' volta para a intro do game
                if event.key == pygame.K_v:
                    pygame.mixer.music.play(-1)
                    conf = False
def IntroDoGame():
    pygame.mixer.music.load("musicas/musica-intro.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    intro = True
    while intro:

        janela.blit(cenario_intro,(0,0))
        #parando música do game
        music.stop()
        informacoes(nomedev,False,font_recorde,pos_texto_dev,False,False)
        informacoes(nome_jogo,False,font_titulo,pos_texto_titulo,False,False)
        informacoes(start,False,font_recorde,pos_texto_start,False,False)
        informacoes(config,False,font_recorde,pos_texto_config,False,False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()
            #Se pressionar uma tecla
            if event.type ==pygame.KEYDOWN:
                #Se pressionar enter sai do loop e entra no game
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    time.sleep(0.4)
                    efeito_start.play(0)
                    intro = False
                if event.key == pygame.K_c:
                    pygame.mixer.music.stop()
                    configuracoes()

        pygame.display.update()
        
def informacoes(mensagem,cor_texto,fonte,posicao_na_tela,condicao,val_do_str):
    texto = fonte.render(mensagem,True,chocolate)
    janela.blit(texto,(posicao_na_tela))
    if condicao == True:
         texto = fonte.render(mensagem  + str(val_do_str), True, cor_texto)
         janela.blit(texto,(posicao_na_tela))


def GameOver():
    time.sleep(0.1)
    efeito_gameover.play(0)
    gameov = True
    while gameov:
        music.stop()
        cenario_gameover = pygame.image.load("imagens/gameover.png")
        janela.blit(cenario_gameover,(0,0))

        #Posições dos retângulos em x e y;
        px1 = pos1_gameover[0]-10
        py1 = pos1_gameover[1]
        px2 = pos2_gameover[0]-35
        py2 = pos2_gameover[1]

        #Criando os retângulos e o texto para exibir
        rect_c = pygame.draw.rect(janela,preto,[px1,py1,200,70])
        informacoes(msg1_gameover,False,font_titulo,pos1_gameover,False,False)
        rect_s = pygame.draw.rect(janela,preto,[px2,py2,170,70])
        informacoes(msg2_gameover,False,font_titulo,pos2_gameover,False,False)
       

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                pygame.quit()

                #Se pressionar algum botão do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Posições do mouse
                x = pygame.mouse.get_pos( )[0]
                y = pygame.mouse.get_pos()[1]
                
                #Se o clique estiver dentro das dimensões dos retângulos
                if x > px1 and y > py1 and x < px1+200 and y < py1+70:
                    pygame.display.update()
                    recorde = 0
                    vidas = 5
                    gameov = False

                if x > px2 and y > py2 and x < px2+170 and y < py2+70:
                    recorde = 0
                    quit()
                    pygame.quit()
                    
        #Carrega as informações na tela            
        pygame.display.update()
            
        

#inicializando pygame
pygame.init()

relogio = pygame.time.Clock()
#Criando janela
janela = pygame.display.set_mode((largura_da_janela,altura_da_janela))
pygame.display.set_caption("Game")
#Criando jogador principal
jogador = {'objRect': pygame.Rect(500,505,largura_do_personagem,altura_do_personagem),'imagem':personagem,'velocidade':velocidade}

#Criando fontes
pygame.font.init()
font_geral = pygame.font.Font("fontes/Valentine.ttf",18)
texto_pedido = font_geral.render(pedido['pedido'],True,vermelho)
texto_nome = font_geral.render(pedido['nome'],True,vermelho)
font_recorde = pygame.font.Font("fontes/Plant.ttf",36)
font_titulo = pygame.font.Font("fontes/Valentine.ttf",30)


#Carregando som
music = pygame.mixer.Sound("musicas/musica1.mp3")
efeito = pygame.mixer.Sound("musicas/colisao.ogg")
som_vitoria = pygame.mixer.Sound("musicas/venceu.ogg")
efeito_q = pygame.mixer.Sound("musicas/perdeu.wav")
efeito_start = pygame.mixer.Sound("musicas/start.mp3")
efeito_gameover = pygame.mixer.Sound("musicas/gameover.mp3")




IntroDoGame()
#Inicializando o loop da janela aberta
while janela_aberta:
    
    #Condições para mudar de cenário
    if recorde >= 100 and recorde < 200:
        cenario = pygame.image.load("imagens/cenario2.png")
        velocidade = 18
    elif recorde >= 200 and recorde < 300:
        cenario = pygame.image.load("imagens/cenario3.png")
        iteracao = 30
        velocidade = 80

    elif recorde >=300 and recorde < 400:
        cenario = pygame.image.load("imagens/cenario4.png")
        iteracao = 20
        iteracao1 = 30

    elif recorde >=400 and recorde < 500:
        cenario = pygame.image.load("imagens/cenario5.png")
        iteracao = 10

    elif recorde >= 500 and recorde < 600:
        cenario = pygame.image.load("imagens/cenario6.png")
        iteracao = 25
        iteracao1 = 35
        velocidade = 80
    elif recorde >=600 and recorde < 700:
        cenario = pygame.image.load("imagens/cenario7.png")
        iteracao = 32
        iteracao1 = 42
        velocidade = 180
    elif recorde >=700 and recorde < 800:
        cenario = pygame.image.load("imagens/cenario8.png")
        iteracao = 11
        iteracao1 = 22
        velocidade = 90

    elif recorde >=800 and recorde < 900:
        cenario = pygame.image.load("imagens/cenario9.png")
        iteracao = 28
        velocidade = 80
    elif recorde >=900 and recorde <1000:
        cenario = pygame.image.load("imagens/cenario10.png")
        iteracao = 5

        velocidade = 90
    elif recorde >= 1000:
        pygame.mixer.music.stop()
        cenario = pygame.image.load("imagens/cenario-venceu.png")
        
        if vez == 0:
            som_vitoria.play(-1)
            

    janela.blit(cenario,(0,0))
    pygame.draw.rect(janela,preto,[0,0,170,60])
    
    #For para pegar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            janela_aberta = False

        #Se a tecla for pressionada
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = True
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = True
            if  evento.key == pygame.K_UP:
                #Contador de vezes q o usuário pediu pra tocar a música
                vez+=1
                music.play(-1)
                musica = True
            if evento.key ==pygame.K_SPACE:
                # Se pressionar 'space' ele entra na Intro e pausa o game;
                IntroDoGame()

            #Se pressionou para desligar a música ou se já estiver tocando, dar stop na música
            if evento.key == pygame.K_DOWN or vez>=2:
                music.stop()
                vez = 0
                musica = False


        #Se a tecla for solta
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas['direita'] = False
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas['esquerda'] = False

    #Chamando função que cria o coração
    contador+=1
    if contador > iteracao:
        contador = 0
        CriaObjetos(lista_coracao,largura_do_coracao,altura_do_coracao,coracao,largura_da_janela)

     #Condição para mudar para o coração que faz perder pontuação
    contador1+=1
    if contador1 > iteracao1:
        contador1 = 0
        CriaObjetos(lista_coracao_q,largura_do_coracao_q,altura_do_coracao_q,coracaoq,largura_da_janela)
        
    #Condição para criar o coração verde que derá vidas ao personagem  
    contador2+=1
    if contador2 > iteracao2:
        contador2 = 0
        CriaObjetos(lista_coracao_v,largura_do_coracao_v,altura_do_coracao_v,coracaov,largura_da_janela)

    #Chamando a função com o personagem principal
    MoverJogador(jogador,teclas,(largura_da_janela,altura_da_janela))
    #Desenhando o personagem
    janela.blit(jogador['imagem'],jogador['objRect'])
    

    #coração quebrado
    informacoes(vds,rosa,font_recorde,pos_vds,True,vidas)
    
    for coraq in lista_coracao_q[:]:
        choqueq = jogador['objRect'].colliderect(coraq['objRect'])
        if choqueq:
            efeito_q.play(0)
            if vidas == 1:
                GameOver()
                #Depois que voltar do GameOver volta com as vidas e
                #as teclas recebem False pra não movimentar o personagem
                
                teclas = {'direita':False,'esquerda':False}
                vidas = 6
                
            #Enquando as vidas forem >1 pode ir descontando    
            if vidas > 1:
                vidas-=1
            
            if recorde >=5:
                #Diminui 5 pontos caso haja colisão com o coração quebrado
                recorde-=5
                informacoes(pts,rosa,font_recorde,pos_pts,True,recorde)
            #Depois do choque remove o coração da lista, pra não pesar o jogo
            lista_coracao_q.remove(coraq)

        if coraq['objRect'].y > altura_da_janela and coraq in lista_coracao_q:
            lista_coracao_q.remove(coraq)

    for coraq in lista_coracao_q:
        MoverCoracao(coraq)
        janela.blit(coraq['imagem'],coraq['objRect'])

    #Coracao vidas
    for corav in lista_coracao_v[:]:
        informacoes(vds,rosa,font_recorde,pos_vds,True,vidas)
        choquev = jogador['objRect'].colliderect(corav['objRect'])
        
        if choquev:
            efeito.play(0)
            
            if vidas >0 and vidas <5:
                vidas+=1
                informacoes(vds,rosa,font_recorde,pos_vds,True,vidas)
                
            #Depois do choque remove o coração da lista, pra não pesar o jogo
            lista_coracao_v.remove(corav)

        if corav['objRect'].y > altura_da_janela and corav in lista_coracao_v:
            lista_coracao_v.remove(corav)

    for corav in lista_coracao_v:
        MoverCoracao(corav)
        janela.blit(corav['imagem'],corav['objRect'])
        
        
    #For para a colisão e a remoção do coração caso ocorra a colisão
    for coracaozinho in lista_coracao[:]:
        choque = jogador['objRect'].colliderect(coracaozinho['objRect'])

        if choque:
            efeito.play(0)
            recorde +=1
            lista_coracao.remove(coracaozinho)
        informacoes(pts,rosa,font_recorde,pos_pts,True,recorde)

        if coracaozinho['objRect'].y > altura_da_janela and coracaozinho in lista_coracao:
            lista_coracao.remove(coracaozinho)

        if recorde>= musica_na_tela and recorde < 200 and musica == True:
            iteracao = 2
            janela.blit(texto_nome,(280,220))
            janela.blit(texto_pedido,(280,250))

    for coracaozinho in lista_coracao:
        MoverCoracao(coracaozinho)
        janela.blit(coracaozinho['imagem'],coracaozinho['objRect'])

    pygame.display.update()
    relogio.tick(FPS)

    

#Finalizando o módulo pygame
pygame.quit()

