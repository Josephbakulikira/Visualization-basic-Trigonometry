import sys
import pygame
from math import cos, sin, tan, pi
from constants import *
from line import Line

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

position = (Width//2, Height//2)
yAxis = Line( [position[0], 0], [position[1], Height], YaxisColor, 1)
xAxis = Line( [0, position[1]], [Width, position[1]], XaxisColor, 1)

# theta in degrees
angle = 0

# toggles
showAxis = True
showPoint = True
showLine = True
showOrigin = True
showCos = True
showSin = True
showTan = True

def toRadian(degree):
    return degree * pi / 180


run = True
while run:
    clock.tick(fps)

    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
    # draw x and y axis
    if showAxis:
        yAxis.Show(screen)
        xAxis.Show(screen)
    # draw main circle
    pygame.draw.circle(screen, circleColor, position, radius, circleStroke)

    # calculate
    theta = toRadian(angle)
    x = radius * cos(theta) # using the polar coordinates
    y = radius * -sin(theta)

    pointPos = [int(x) + position[0], int(y) + position[1]] # center the x and y pos

    secante = radius/cos(theta)

    sinLine  = Line( pointPos, [pointPos[0], position[1]], SinColor, 3)
    cosLine  = Line( pointPos, [position[0], pointPos[1]], CosColor, 3)
    tanLine  = Line( pointPos, [position[0] +secante , position[1]], TanColor, 3)
    ctanLine = Line( pointPos, [], CtanColor, 3)
    #--lines---
    if showCos:
        cosLine.Show(screen)

    if showSin:
        sinLine.Show(screen)

    if showTan:
        tanLine.Show(screen)
    #draw line from the origin to the point
    if showLine:
        pygame.draw.line(screen, lineColor, position, pointPos, 2 )
    #draw origin:
    if showOrigin:
        pygame.draw.circle(screen, OriginColor, position, 5)
    #draw moving point
    if showPoint:
        pygame.draw.circle(screen, PointColor, pointPos, 10)
    pygame.display.update()
    angle += speed+0.4

pygame.quit()
sys.exit()
