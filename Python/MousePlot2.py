import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def map_value(current_min, current_max, new_min, new_max, value):
    """
    Translate between different coordinate systems
    A/(current_max - current_min) == B/(new_max - new_min)
    """
    current_range = current_max - current_min
    new_range = new_max - new_min
    return new_min + new_range * ((value - current_min) / current_range)
  
pygame.init()
# two different coord systems for pygame and OpenGL
screen_width, screen_height = 1000, 800
ortho_width, ortho_height = 640, 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, 0, ortho_height)


def plot_point():
    glBegin(GL_POINTS)

    for p in points:
        glVertex2f(p[0], p[1])

    glEnd()


done = False
init_ortho()
glPointSize(5)

points = []

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, 0, ortho_width, p[0]),
                           map_value(0, screen_height, ortho_height, 0, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    plot_point()

    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
