# Subscribe to my youtube
# Youtube Channel: http://www.youtube.com/channel/UCjPk9YDheKst1FlAf_KSpyA?sub_confirmation=1
import sys
import pygame
from math import cos, sin, tan, pi
from constants import *
from line import Line
from parameters import *
import colorsys
from event import HandleEvent

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

position = (Width//2, Height//2)
yAxis = Line( [position[0], 0], [position[0], Height], YaxisColor, 1)
xAxis = Line( [0, position[1]], [Width, position[1]], XaxisColor, 1)

Xwave = []
Ywave = []

previousRadius = radius
previousSpeed = radius
# theta in degrees
angle = 0.0001

def toRadian(degree):
    return degree * pi / 180

def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

clicked = False
run = True
while run:
    clock.tick(fps)
    run, clicked, pause, showUI = HandleEvent(clicked, pause, showUI)
    #theme
    backgroundColor = (4, 4, 8) if Dark == True else (255, 255, 255)
    circleColor = (255, 255, 255) if Dark == True else (0, 0, 0)
    PointColor = (255, 255, 255) if Dark == True else (0, 0, 0)
    lineColor = (255, 255, 255) if Dark == True else (0, 0, 0)
    if Dark == False:
        panel.alpha = 200
    else:
        panel.alpha = 100

    screen.fill(backgroundColor)


    if previousRadius != radius or previousSpeed != speed:
        Xwave.clear()
        Ywave.clear()

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
    CscLine  = Line( position, [position[0]  , position[1] - cosecante], CscColor, 3, "csc", "Left")

    if pause==False:
        Xwave.insert(0, pointPos[1])
        Ywave.insert(0, pointPos[0])
        if len(Xwave) > limit:
            Xwave.pop()
            Ywave.pop()

    #draw waves
    if offsetWaves == False:
        waveOffset = 0

    else:
        waveOffset = radius
    if showXwave:
        for i in range(len(Xwave)):
                pygame.draw.circle(screen, XwaveColor, (i+ position[0]+waveOffset, Xwave[i]), 2)
                pygame.draw.circle(screen, XwaveColor, (position[0]-i-waveOffset, Xwave[i]), 2)

    if showYwave:
        for i in range(len(Ywave)):
            pygame.draw.circle(screen, YwaveColor, (Ywave[i], position[1] + waveOffset + i), 2)
            pygame.draw.circle(screen, YwaveColor, (Ywave[i], position[1] - waveOffset - i), 2)=
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

        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render(str(round(angle, 2)) + " °", True, circleColor)
        textRect = text.get_rect()
        p = (position[0]-offset, position[1]-offset)
        textRect.center = (position[0]+offset, position[1]-offset)
        pygame.draw.arc(screen, OriginColor, [p[0], p[1], angleArc, angleArc], 2*pi, theta, 2)
        screen.blit(text, textRect)

    #draw line from the origin to the point
    if showLine:
        pygame.draw.line(screen, lineColor, position, pointPos, 4 )
    #draw origin:
    if showOrigin:
        pygame.draw.circle(screen, OriginColor, position, 5)
    #draw moving point
    if showPoint:
        PointColor = hsv_to_rgb(angle/140, 1, 1)
        pygame.draw.circle(screen, PointColor, pointPos, 10)

    previousRadius = radius
    previousSpeed = speed
    # -- draw ui ---
    if showUI:
        # text
        panel.Render(screen)
        CosText.Render(screen)
        SinText.Render(screen)
        TanText.Render(screen)
        CoText.Render(screen)
        SecText.Render(screen)
        CosecText.Render(screen)
        SinWaveText.Render(screen)
        CosWaveText.Render(screen)
        WOffsetText.Render(screen)
        AngleText.Render(screen)
        PressSpaceText.Render(screen)
        LineText.Render(screen)
        RadiusText.Render(screen)
        SpeedText.Render(screen)
        DarkText.Render(screen)
        #toggle buttons
        showSin = SinToggle.Render(screen, clicked)
        showCos = CosToggle.Render(screen, clicked)
        showTan = TanToggle.Render(screen, clicked)
        showCtan = CoToggle.Render(screen, clicked)
        showSec = SecToggle.Render(screen, clicked)
        showCsc = CscToggle.Render(screen, clicked)
        showXwave = SinWaveToggle.Render(screen, clicked)
        showYwave = CosWaveToggle.Render(screen, clicked)
        offsetWaves = OffsetToggle.Render(screen, clicked)
        showTheta = AngleToggle.Render(screen, clicked)
        showLine = LineToggle.Render(screen, clicked)
        Dark = DarkToggle.Render(screen, clicked)
        #slider buttons
        radius = RadiusSlider.Render(screen)
        speed = speedSlider.Render(screen)
    else:
        UItoggle.Render(screen)

    pygame.display.update()
    if pause==False:
        angle += speed
        if angle >= 360:
            angle = 0.0001
    #UItoggle.fontSize = int( sin(angle/3) +24)
    clicked = False
pygame.quit()
sys.exit()
