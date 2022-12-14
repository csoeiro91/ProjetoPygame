import pygame
from pygame import display
from pygame.transform import scale
from pygame.image import load
from pygame.sprite import Sprite

pygame.init()

tamanho = 800,600 #variável que absorve o tamanho do plano em X e Y
superficie = display.set_mode((tamanho)) #variável que absorve a contrução do plano.
display.set_caption('O  Homem Aranha') #funcão que escreve o nome da janela.

fundo = scale(load('images/cidade.jpg'), tamanho) #como a imagem é maior que o plano, usamos a função SCALE para transformar a imagem no tamanho do plano.

class HomemAranha(Sprite): #criamos o primeiro sprint que irá compor o jogo, o objeto principal.
    def __init__(self):
        super().__init__() #defino essa função será usada em outras classes como herança.

        self.image = load('images/homemaranha_small.png') #carrego a imagem e em seguida tranfiro para uma variável.
        self.rect = self.image.get_rect() #uso a função get_rect na imagem, onde irá me permitir o movimento no plano.


# Espaço do display
superficie.blit(fundo, (0, 0)) #Faço o Bit Blit na imagem no ponto 0,0 do plano definimo, com isso consigo inserir a imagem no jogo.

display.update() # a função update atualiza os frames.

while True:
     ...