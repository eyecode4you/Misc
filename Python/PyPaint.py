"""
PyPaint - A very simple paint program built in Python 

Controls:
spacebar - clear screen
s - save current drawing
l - load saved drawing
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Utils import *

pygame.init()

screen_width, screen_height = 1000, 800
ortho_left, ortho_right, ortho_top, ortho_bottom = 0, 4, -1, 1

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('PyOpenGL Sketchpad')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)


def plot_point():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_lines():
    for l in points:
        glBegin(GL_LINE_STRIP)
        for coords in l:
            glVertex2f(coords[0], coords[1])
        glEnd()


def save_drawing():
    """ Save line coords of user drawing into a txt file """
    f = open("drawing.txt", "w")
    f.write(str(len(points)) + "\n")  # no. of lines
    for l in points:
        f.write(str(len(l)) + "\n")  # no. of points
        for coords in l:
            f.write(str(coords[0]) + " " + str(coords[1]) + "\n")  # coords
    f.close()
    print("Drawing saved...")


def load_drawing():
    """ Load line coords of user drawing to screen """
    f = open("drawing.txt", "r")
    num_of_lines = int(f.readline())
    global points, line
    points = []
    for l in range(num_of_lines):
        line = []
        points.append(line)
        num_of_coords = int(f.readline())
        for coord_number in range(num_of_coords):
            px, py = [float(value) for value in next(f).split()]
            line.append((px, py))
    print("Drawing loaded...")


def clear_drawing():
    """ Clear line coords of user drawing """
    global points
    points = []
    print("Drawing Cleared...")


m_down, done = False, False
init_ortho()
glPointSize(2)

points, line = [], []

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_drawing()
            if event.key == pygame.K_l:
                load_drawing()
            if event.key == pygame.K_SPACE:
                clear_drawing()
        elif event.type == MOUSEBUTTONDOWN:
            m_down = True
            line = []
            points.append(line)
        elif event.type == MOUSEBUTTONUP:
            m_down = False
        elif event.type == MOUSEMOTION and m_down:
            p = pygame.mouse.get_pos()
            line.append((map_value(0, screen_width, ortho_left, ortho_right, p[0]),
                         map_value(0, screen_height, ortho_bottom, ortho_top, p[1])))

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    plot_lines()

    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
