import pygame
from pygame import display
from pygame.transform import scale
from pygame.image import load
from pygame import font
from pygame.sprite import Sprite

pygame.init()

tamanho = 800,600
fonte = font.SysFont('arial', 24)
fonte_perdeu = font.SysFont('arial', 50)

superficie = display.set_mode((tamanho))
display.set_caption('O  Homem Aranha')

fundo = scale(
    load('images/cidade.jpg'),
    tamanho
)


class HomemAranha(Sprite):
    def __init__(self, teia):
        super().__init__()

        self.image = load('images/homemaranha_small.png')
        self.rect = self.image.get_rect()
        self.teia = teia
        self.velocidade = 4

    def atirar_teia(self):
        if len(self.teia) < 15:
            self.teia.add(
                Teia(*self.rect.center)
            )

    def update(self):
        keys = pygame.key.get_pressed()

        teiaDisponivel_fonte = fonte.render(
            f'Teias: {15 - len(self.teia)}',
            True,
            (255, 255, 255)
        )
        superficie.blit(teiaDisponivel_fonte, (20, 20))

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocidade

class Teia(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = load('images/teia_small.png')
        self.rect = self.image.get_rect(
            center=(x, y)
        )

# Espaço do display
superficie.blit(fundo, (0, 0))

display.update()

while True:
     ...