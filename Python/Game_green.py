#Crie um jogo aonde o fundo é verde e o personagem do jogo é um quadrado vermelho.
#Adicione a ele a capacidade de se movimentar.
#E adicione uma tecla que quando clicada mnude a cor do quadrado para uma aleatoria.

import pygame
import pygame.display
import random

pygame.init()

vermelho = (245, 0 , 35)
verde = (25, 255, 0)
azul = (50, 150, 245)

largura = 850
altura = 700
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("jogo do quadrado vermelhão")

gay_pos = [largura / 2, altura / 2]
gay_tamanho = 30

cor_quadrado = vermelho

font = pygame.font.Font(None, 36)

corrida = True

while corrida:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corrida = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        gay_pos[0] -= 1
    if keys[pygame.K_RIGHT]:
        gay_pos[0] += 1
    if keys[pygame.K_UP]:
        gay_pos[1] -= 1
    if keys[pygame.K_DOWN]:
        gay_pos[1] += 1

    gay_pos[0] = max(0, min(largura - gay_tamanho, gay_pos[0]))
    gay_pos[1] = max(0, min(altura - gay_tamanho, gay_pos[1]))

    if keys[pygame.K_SPACE]:
        cor_quadrado = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0,255)
        )

    janela.fill(verde)

    pygame.draw.rect(janela, cor_quadrado, (*gay_pos, gay_tamanho, gay_tamanho))

    pygame.display.flip()

pygame.quit()