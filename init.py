import sys, pygame
import numpy as np
from scipy.integrate import odeint

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COL = (180, 32, 105)

m1 = 20
l1 = 30
m2 = 20
l2 = 30
g = 10
init_angle_1 = 45
init_angle_2 = 70

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class Pendulum(pygame.sprite.Sprite):
    angle = 0
    angvel = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, angle) #superclass constructor
        
        self.image = pygame.Surface([20,20])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, COL, self.rect.center, 20)

# equations from https://web.mit.edu/jorloff/www/chaosTalk/double-pendulum/double-pendulum-en.html
def delangvel1(angle1, angle2, av1, av2):
    top = (-1 * g * (2 * m1 + m2) * np.sin(angle1)) - m2 * g * np.sin(angle1 - 2 * angle2) - 2 * np.sin(angle1 - angle2) * m2 * (av2 * av2 * l2 + av1 * av1 * l1 * np.cos(angle1 - angle2))
    bottom = l1 * (2 * m1 + m2 - m2 * np.cos(2 * (angle1 - angle2)))
    return (top / bottom)

def delangvel2(angle1, angle2, av1, av2):
    top = 2 * np.sin(angle1 - angle2) * (av1 * av1 * l1 * (m1 + m2) + g*(m1 + m2) * np.cos(angle1) + av2 * av2 * l2 * m2 * np.cos(angle1 - angle2))
    bottom = l2 * (2 * m1 + m2 - m2 * np.cos(2 * (angle1 - angle2)))
    return (top / bottom)

def move((basex, basey), length, delang):
    dely = length * np.sin(delang)
    newy = basey - dely
    newx = dely / np.tan(delang)
    return (newx, newy)

pendulum1 = Pendulum(init_angle_1)
pendulum2 = Pendulum(init_angle_2)

clock = pygame.time.Clock()
while 1:
    clock.tick(60)
    screen.fill((0, 0, 0)) # easiest way to draw trails is to make this semi-transparent, but the arms need to be hidden
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    

