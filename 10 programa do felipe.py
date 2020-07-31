import pygame
import random
BLACK = (0,0,0)
WHITE = (255,255,255)
pygame.init()
screen = pygame.display.set_mode([800,600)]
pygame.display.set_caption("Pop a Smiley")
mousedown = False
keep_going = True
clock = pygame.time.Clock()
pic = pygame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey)
sprite_list = pygame.sprite.Group()
pygame.mixer.init()   # Adisiona sons
pop = pygame.mixer.Sound("pop.wav")
font = pygame.font.SysFont("Arial", 24)
count_smileys = 0
count_popped = 0
class Smiley(pygame.sprite.Sprite):
    pos = (0,0)
    xvel  = 1
    scale = 100
    def _init_(self, pos, xvel,yvel):
