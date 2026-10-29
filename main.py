import pygame

from game.inventario import Inventario
from game.player import Jogador
from game.inimigo import Inimigo
from game.mapa import Mapa

pygame.init()

# Tamanho de cada casa do mapa
TAMANHO_CASA = 40

# Dimensões do mundo
COLUNAS = 40
LINHAS = 30

# Área visível na tela
LARGURA = 800
ALTURA_JOGO = 600
ALTURA_HUD = 80
ALTURA = ALTURA_JOGO + ALTURA_HUD

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simple Roguelike")

relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 28)

mapa = Mapa(COLUNAS, LINHAS)

jogador_x, jogador_y = mapa.centro_sala(1)
inimigo_x, inimigo_y = mapa.centro_sala(2)

jogador = Jogador(
    nome="Aventureiro",
    idade=20,
    vida=100,
    x=jogador_x,
    y=jogador_y
)

inimigo = Inimigo(
    nome="Goblin",
    idade=5,
    vida=60,
    x=inimigo_x,
    y=inimigo_y
)

jogador.vida_maxima = jogador.vida

inventario = Inventario()
inventario_aberto = False

executando = True
mensagem = "Explore a masmorra!"
vitoria = False


def desenhar_personagem(personagem):
    x = personagem.x * TAMANHO_CASA
    y = personagem.y * TAMANHO_CASA

    pygame.draw.rect(
        tela,
        personagem.cor,
        (x + 4, y + 4, TAMANHO_CASA - 8, TAMANHO_CASA - 8),
        border_radius=6
    )


def desenhar_texto(texto, x, y, cor=(255, 255, 255)):
    imagem = fonte.render(texto, True, cor)
    tela.blit(imagem, (x, y))

def calcular_camera(jogador):
    # Centro do jogador em pixels.
    jogador_px = jogador.x * TAMANHO_CASA + TAMANHO_CASA // 2
    jogador_py = jogador.y * TAMANHO_CASA + TAMANHO_CASA // 2

    # Tenta manter o jogador no centro da tela.
    camera_x = jogador_px - LARGURA // 2
    camera_y = jogador_py - ALTURA_JOGO // 2

    # Impede que a câmera saia dos limites do mapa.
    largura_mapa = COLUNAS * TAMANHO_CASA
    altura_mapa = LINHAS * TAMANHO_CASA

    camera_x = max(0, min(camera_x, largura_mapa - LARGURA))
    camera_y = max(0, min(camera_y, altura_mapa - ALTURA_JOGO))

    return camera_x, camera_y

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                executando = False

                  # Abre ou fecha o inventario.
            if evento.key == pygame.K_i:
                inventario_aberto = not inventario_aberto
                continue

            # Enquanto o inventario estiver aberto,
            # somente permitimos usar itens ou fecha-lo.
            if inventario_aberto:
                if evento.key == pygame.K_1:
                    if jogador.vida > 0 and inimigo.vida > 0:
                        usou = inventario.usar_pocao(jogador)

                        if usou:
                            mensagem = "Voce usou uma pocao de vida!"

                            # Usar um item consome um turno.
                            inimigo.agir(jogador, mapa)

                        elif inventario.itens["Pocao de vida"] <= 0:
                            mensagem = "Voce nao tem mais pocoes!"

                        elif jogador.vida >= jogador.vida_maxima:
                            mensagem = "Sua vida ja esta cheia!"

                continue

            # Só aceitamos ações enquanto a partida estiver ativa.
            if jogador.vida > 0 and inimigo.vida > 0:
                dx, dy = 0, 0

                if evento.key in (pygame.K_w, pygame.K_UP):
                    dy = -1
                elif evento.key in (pygame.K_s, pygame.K_DOWN):
                    dy = 1
                elif evento.key in (pygame.K_a, pygame.K_LEFT):
                    dx = -1
                elif evento.key in (pygame.K_d, pygame.K_RIGHT):
                    dx = 1

               
                if dx != 0 or dy != 0:
                    destino = (
                        jogador.x + dx,
                        jogador.y + dy
                    )

                    turno_consumido = False

                    if destino == (inimigo.x, inimigo.y):
                        inimigo.receber_dano(jogador.ataque)
                        mensagem = (
                            f"Voce atacou o Goblin "
                            f"com {jogador.ataque} de dano!"
                        )
                        turno_consumido = True

                    else:
                        moveu = jogador.mover(dx, dy, mapa)

                        if moveu:
                            mensagem = "Voce se movimentou."
                            turno_consumido = True

                    if turno_consumido and inimigo.vida > 0:
                        inimigo.agir(jogador, mapa)

     # Calcula a posição da câmera.
    camera_x, camera_y = calcular_camera(jogador)

    # Desenha somente a área visível do mapa.
    tela.fill((30, 30, 38))

    for y in range(LINHAS):
        for x in range(COLUNAS):
            tela_x = x * TAMANHO_CASA - camera_x
            tela_y = y * TAMANHO_CASA - camera_y

            retangulo = pygame.Rect(
                tela_x,
                tela_y,
                TAMANHO_CASA,
                TAMANHO_CASA
            )

            # Não desenha casas fora da área de jogo.
            if not retangulo.colliderect(
                pygame.Rect(0, 0, LARGURA, ALTURA_JOGO)
            ):
                continue

            if (x, y) in mapa.paredes:
                pygame.draw.rect(
                    tela, (110, 110, 125), retangulo
                )
            else:
                pygame.draw.rect(
                    tela, (45, 45, 55), retangulo
                )

            pygame.draw.rect(
                tela, (58, 58, 68), retangulo, 1
            )

    # Desenha personagens com o deslocamento da câmera.
    def desenhar_personagem_na_camera(personagem):
        x = personagem.x * TAMANHO_CASA - camera_x
        y = personagem.y * TAMANHO_CASA - camera_y

        pygame.draw.rect(
            tela,
            personagem.cor,
            (
                x + 4,
                y + 4,
                TAMANHO_CASA - 8,
                TAMANHO_CASA - 8
            ),
            border_radius=6
        )

    if inimigo.vida > 0:
        desenhar_personagem_na_camera(inimigo)

    if jogador.vida > 0:
        desenhar_personagem_na_camera(jogador)

    # HUD fixa: a câmera não desloca esta parte.
    pygame.draw.rect(
        tela,
        (20, 20, 26),
        (0, ALTURA_JOGO, LARGURA, ALTURA_HUD)
    )

    desenhar_texto(
        f"{jogador.nome} - Vida: {jogador.vida}",
        15, ALTURA_JOGO + 10
    )

    desenhar_texto(
        f"Goblin - Vida: {inimigo.vida}",
        15, ALTURA_JOGO + 40,
        (255, 120, 120)
    )

    if jogador.vida <= 0:
        desenhar_texto(
            "Voce morreu! Feche a janela para sair.",
            400, ALTURA_JOGO + 10,
            (255, 90, 90)
        )
    elif inimigo.vida <= 0:
        desenhar_texto(
            "Vitoria! Voce derrotou o Goblin.",
            400, ALTURA_JOGO + 10,
            (120, 255, 120)
        )
    else:
        desenhar_texto(
            mensagem,
            400, ALTURA_JOGO + 40
        )

        # Janela do inventario.
    if inventario_aberto:
        largura_janela = 420
        altura_janela = 260

        janela_x = (LARGURA - largura_janela) // 2
        janela_y = (ALTURA_JOGO - altura_janela) // 2

        pygame.draw.rect(
            tela,
            (25, 25, 35),
            (janela_x, janela_y, largura_janela, altura_janela),
            border_radius=12
        )

        pygame.draw.rect(
            tela,
            (180, 180, 200),
            (janela_x, janela_y, largura_janela, altura_janela),
            width=2,
            border_radius=12
        )

        desenhar_texto(
            "INVENTARIO",
            janela_x + 20,
            janela_y + 20
        )

        desenhar_texto(
            f"1 - Pocao de vida: "
            f"{inventario.itens['Pocao de vida']}",
            janela_x + 20,
            janela_y + 75,
            (120, 255, 140)
        )

        desenhar_texto(
            "Recupera ate 30 pontos de vida",
            janela_x + 20,
            janela_y + 115
        )

        desenhar_texto(
            "Pressione I para fechar",
            janela_x + 20,
            janela_y + 200,
            (200, 200, 200)
        )

    pygame.display.flip()

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
