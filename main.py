import sys
import pygame
from math import cos, sin, tan, pi
from constants import *
from line import Line
from parameters import *

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

position = (Width//2, Height//2)
yAxis = Line( [position[0], 0], [position[0], Height], YaxisColor, 1)
xAxis = Line( [0, position[1]], [Width, position[1]], XaxisColor, 1)

# theta in degrees
angle = 0.0001


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
    cosecante = radius/sin(theta)

    sinLine  = Line( pointPos, [pointPos[0], position[1]], SinColor, 3, "sin", "Right")
    cosLine  = Line( pointPos, [position[0], pointPos[1]], CosColor, 3, "cos", "Top")
    tanLine  = Line( pointPos, [position[0] + secante , position[1]], TanColor, 3, "tan", "Top")
    ctanLine = Line( pointPos, [position[0], + position[1]-cosecante], CtanColor, 3, "cotan", "Top")
    SecLine  = Line( position, [position[0] + secante , position[1]], SecColor, 3, "sec", "Bottom")
    CscLine  = Line( position, [position[0]  , position[1] - cosecante], CscColor, 3, "cos", "Left")


    #--lines---
    if showCos:
        cosLine.Show(screen)
    if showSin:
        sinLine.Show(screen)
    if showTan:
        tanLine.Show(screen)
    if showCtan:
        ctanLine.Show(screen)
    if showSec:
        SecLine.Show(screen)
    if showCsc:
        CscLine.Show(screen)

    if showTheta:
        offset = angleArc//2

        font = pygame.font.Font('freesansbold.ttf', 12)
        text = font.render(str(round(angle, 2)) + " °", True, OriginColor)
        textRect = text.get_rect()
        p = (position[0]-offset, position[1]-offset)
        textRect.center = (position[0]+offset, position[1]-offset)
        pygame.draw.arc(screen, OriginColor, [p[0], p[1], angleArc, angleArc], 2*pi, theta, 2)
        screen.blit(text, textRect)

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
    angle += speed
    if angle >= 360:
        angle = 0.0001

pygame.quit()
sys.exit()
