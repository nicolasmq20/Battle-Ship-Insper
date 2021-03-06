# ------ Gerando caminho para bibliotecas
import sys
import pygame
sys.path.insert(1, 'resources/config')
sys.path.insert(1, 'resources/telas')
# ------ Importando bibliotecas
from TelaInicial import tela_inicial
from TelaJogo import tela_jogo
from TelaFinal import tela_final
from config import HEIGHT, WIDTH, QUIT, TELA_INICIAL, GAME, TELA_FINAL

# ------ inicia pygame
pygame.init()
pygame.mixer.init()

# ------ Gera a Tela de jogo
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Battle Ship - O Retono ao Presencial')
pygame.display.set_icon(pygame.image.load('resources/img/gameicon.png'))

# ====== Rotina principal o jogo: =========
estado = TELA_INICIAL
resultado = 0
vitoria = 0

while estado != QUIT:
    if estado == TELA_INICIAL:
        estado = tela_inicial(TELA)
    if estado == GAME:
        resultado = tela_jogo(TELA)
        estado = resultado [0]
        vitoria = resultado [1]
    if estado == TELA_FINAL:
        estado = tela_final(TELA, vitoria)


# ----- Finaliza o jogo
pygame.quit()