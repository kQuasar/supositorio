#Crie um jogo aonde o fundo é verde e o personagem do jogo é um quadrado vermelho.
#Adicione a ele a capacidade de se movimentar.
#E adicione uma tecla que quando clicada mnude a cor do quadrado para uma aleatoria.

import pygame
import pygame.display
import random

class Quadrado (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.cor_quadrado = (250, 95, 95)
        self.largura = 50
        self.altura = 50
        self.gay_tamanho = 30
        self.homofobico = (self.largura / 2, self.altura / 2)
        self.image = pygame.Surface(size = self.homofobico)
        self.image.fill(self.cor_quadrado)
        self.rect = self.image.get_rect(center = (425, 350))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2
        if keys[pygame.K_UP]:
            self.rect.y -= 2

                

        

pygame.init() 

vermelho = (245, 0 , 35)
verde = (0, 155, 0)
azul = (50, 150, 245)

largura = 850
altura = 700
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("jogo do quadrado vermelhão") 

font = pygame.font.Font(None, 36)

variavel = Quadrado()

valor = pygame.sprite.Group()
valor.add(variavel)
time = pygame.time.Clock()
corrida = True

while corrida:
    for event in pygame.event.get():
        if event.type == pygame.K_SPACE:
                variavel.image.fill((random.randint(1, 255),random.randint(1, 255),random.randint(1, 255)))
        if event.type == pygame.QUIT:
            corrida = False

    
    valor.update()
    
    janela.fill(verde)
    valor.draw(janela)


    pygame.display.update()

    time.tick(60)
pygame.quit()