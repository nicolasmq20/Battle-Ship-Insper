import pygame
from TelaInicial import tela_inicial
from TelaFinal import tela_final
from config import HEIGHT, WIDTH, QUIT, TELA_INICIAL, GAME, TELA_FINAL

# ------ inicia pygame
pygame.init()

# ------ Gera a Tela de jogo
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Battle Ship')

#===== Rotina principal o jogo:
estado = TELA_INICIAL
resultado = 0
VITORIA = 0

while estado != QUIT:
    if estado == TELA_INICIAL:
        estado = tela_inicial(TELA)
    if estado == GAME:
        resultado = tela_jogo(TELA)
        estado = resultado [0]
        VITORIA = resultado [1]
    if estado == TELA_FINAL:
        estado = tela_final(TELA, VITORIA)


# ----- Finaliza o jogo
pygame.quit()
