import pygame
import time
import random

pygame.init()

# Definição das cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

clock = pygame.time.Clock()
tamanho_cobra = 10
velocidade = 15

fonte = pygame.font.SysFont(None, 25)


def cobra(tamanho_cobra, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho_cobra, tamanho_cobra])


def mensagem(msg, cor):
    tela_texto = fonte.render(msg, True, cor)
    tela.blit(tela_texto, [largura_tela / 2, altura_tela / 2])


def jogo():
    game_over = False
    game_fim = False

    x1 = largura_tela / 2
    y1 = altura_tela / 2

    x1_mudar = 0
    y1_mudar = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura_tela - tamanho_cobra) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_cobra) / 10.0) * 10.0

    while not game_over:
        while game_fim:
            tela.fill(branco)
            mensagem("Fim do jogo! Pressione C para jogar novamente ou Q para sair", vermelho)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_fim = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_mudar = -tamanho_cobra
                    y1_mudar = 0
                elif event.key == pygame.K_RIGHT:
                    x1_mudar = tamanho_cobra
                    y1_mudar = 0
                elif event.key == pygame.K_UP:
                    y1_mudar = -tamanho_cobra
                    x1_mudar = 0
                elif event.key == pygame.K_DOWN:
                    y1_mudar = tamanho_cobra
                    x1_mudar = 0

        if x1 >= largura_tela or x1 < 0 or y1 >= altura_tela or y1 < 0:
            game_fim = True

        x1 += x1_mudar
        y1 += y1_mudar
        tela.fill(branco)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                game_fim = True

        cobra(tamanho_cobra, lista_cobra)
        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura_tela - tamanho_cobra) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_cobra) / 10.0) * 10.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()


jogo()