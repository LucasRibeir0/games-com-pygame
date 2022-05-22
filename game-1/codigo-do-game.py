import pygame,random
#Mensagem para exibir informações sobre o desenvolvedor do jogo no terminal
desenvolvedor = {'Desenvolvedor: ':'Lucas Ribeiro Goncalves','Instagram:':'@L_rib3ir0'}
for k,v in desenvolvedor.items():
    print(f'{k} {v}')

#Carregando as imagens que serão usadas no game
personagem = pygame.image.load("imagens/avatar.png")
cenario = pygame.image.load("imagens/cenario1.png")
coracao = pygame.image.load("imagens/coracao.png")
coracaoq = pygame.image.load("imagens/coracao-q.png")
#Pegando largura e altura dos objetos criados
largura_da_janela = cenario.get_width()
altura_da_janela = cenario.get_height()
largura_do_personagem = personagem.get_width()
altura_do_personagem = personagem.get_height()
largura_do_coracao = coracao.get_width()
altura_do_coracao = coracao.get_height()
largura_do_coracao_q = coracaoq.get_width()
altura_do_coracao_q = coracaoq.get_height()
#Criando outras variáveis
velocidade = 8
iteracao = 35
iteracao1 = 50
contador = contador1 = vez = recorde = 0
lista_coracao = []
lista_coracao_q = []
janela_aberta = True
vermelho = (139,0,0)
rosa = (255,20,147)
preto = (28,28,28)
musica_na_tela = 50
pedido = {'nome':'"O coracao','pedido':'tem razoes que a propria razao desconhece".'}
teclas = {'direita':False,'esquerda':False}
musica = False


#Função do movimento do avatar
def MoverJogador(jogador,teclas,dimensoes):
    borda_esquerda = 0
    borda_direita = dimensoes[0]
    if teclas['esquerda'] and jogador['objRect'].left > borda_esquerda:
        jogador['objRect'].x -= jogador['velocidade']
    if teclas['direita'] and jogador['objRect'].right < borda_direita:
        jogador['objRect'].x += jogador['velocidade']
#Movimento do coração
def MoverCoracao(coracao):
    coracao['objRect'].y += coracao['velocidade']
    


def CriaObjetos(lista_objeto,largura_objeto,altura_objeto,img_objeto, largura_janela):
    #Construindo os corações e colocando na lista
        posx = random.randint(0, largura_janela-largura_objeto)
        posy = -altura_objeto
        vel_random = random.randint(3,8)
        #Colocando os objetos na lista
        lista_objeto.append({'objRect':pygame.Rect(posx,posy,largura_objeto,altura_objeto),'imagem':img_objeto,'velocidade':vel_random})


def ExibePontuacao():
    texto_recorde = font_recorde.render("Pontuação: " + str(recorde), True, rosa)
    janela.blit(texto_recorde, ((largura_da_janela / 2.5), 0))

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
font_pedido = pygame.font.Font("fontes/Valentine.ttf",18)
texto_pedido = font_pedido.render(pedido['pedido'],True,vermelho)
texto_nome = font_pedido.render(pedido['nome'],True,vermelho)
font_recorde = pygame.font.Font("fontes/Plant.ttf",36)
texto_recorde = font_recorde.render("Pontuação: " + str(recorde),True,rosa)

#Carregando som
music = pygame.mixer.Sound("musicas/musica1.mp3")
efeito = pygame.mixer.Sound("musicas/colisao.ogg")
som_vitoria = pygame.mixer.Sound("musicas/venceu.ogg")
efeito_q = pygame.mixer.Sound("musicas/perdeu.wav")


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
        iteracao1 = 55
        
    elif recorde >=400 and recorde < 500:
        cenario = pygame.image.load("imagens/cenario5.png")
        iteracao = 10
        
    elif recorde >= 500 and recorde < 600:
        cenario = pygame.image.load("imagens/cenario6.png")
        iteracao = 25
        iteracao1 = 62
        velocidade = 80
    elif recorde >=600 and recorde < 700:
        cenario = pygame.image.load("imagens/cenario7.png")
        iteracao = 32
        iteracao1 = 75
        velocidade = 180
    elif recorde >=700 and recorde < 800:
        cenario = pygame.image.load("imagens/cenario8.png")
        iteracao = 11
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
        cenario = pygame.image.load("imagens/cenario-venceu.png")
        if vez == 0:
            som_vitoria.play(-1)

    janela.blit(cenario,(0,0))
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
    
    
        
    #Chamando a função com o personagem principal
    MoverJogador(jogador,teclas,(largura_da_janela,altura_da_janela))
    #Desenhando o personagem
    janela.blit(jogador['imagem'],jogador['objRect'])


    #coração quebrado
    for coraq in lista_coracao_q[:]:
        choqueq = jogador['objRect'].colliderect(coraq['objRect'])
        if choqueq:
            efeito_q.play(0)
            if recorde >=5:
                #Diminui 5 pontos caso haja colisão com o coração quebrado
                recorde-=5
                ExibePontuacao()
            #Depois do choque remove o coração da lista, pra não pesar o jogo
            lista_coracao_q.remove(coraq)
            
        if coraq['objRect'].y > altura_da_janela and coraq in lista_coracao_q:
            lista_coracao_q.remove(coraq)
            
    for coraq in lista_coracao_q:
        MoverCoracao(coraq)
        janela.blit(coraq['imagem'],coraq['objRect'])
                                        
                                    
    
    #For para a colisão e a remoção do coração caso ocorra a colisão
    for coracaozinho in lista_coracao[:]:
        choque = jogador['objRect'].colliderect(coracaozinho['objRect'])

        if choque:
            efeito.play(0)
            recorde +=1
            lista_coracao.remove(coracaozinho)
        ExibePontuacao()

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
    relogio.tick(35)
    

#Finalizando o módulo pygame
pygame.quit()

