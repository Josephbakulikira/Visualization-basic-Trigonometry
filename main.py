# Subscribe to my youtube
# Youtube Channel: http://www.youtube.com/c/Auctux?sub_confirmation=1
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

Xwave = [] # sin wave
Ywave = [] # cos wave
TanGraph= []
SecWave = []
CscWave = []

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
    dt = clock.tick(fps)/100
    frameRate = clock.get_fps()
    pygame.display.set_caption(str(frameRate) + " fps")

    #handle events
    run, clicked, pause, showUI, showValues = HandleEvent(clicked, pause, showUI, showValues)

    #theme
    backgroundColor = (4, 4, 8) if Dark == True else (255, 255, 255)
    circleColor = (255, 255, 255) if Dark == True else (0, 0, 0)
    PointColor = (255, 255, 255) if Dark == True else (0, 0, 0)
    lineColor = (255, 255, 255) if Dark == True else (0, 0, 0)
    panel.alpha = 80 if Dark == True else 200
    valueColor = (255, 255, 255) if Dark == True else (0, 0, 0)
    screen.fill(backgroundColor)

    if previousRadius != radius or previousSpeed != speed:
        Xwave.clear()
        Ywave.clear()
        TanGraph.clear()
        SecWave.clear()
        CscWave.clear()

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
    tan_val = radius * (sin(theta)/cos(theta))
    cotan_val = radius * (cos(theta)/sin(theta))

    sinLine  = Line( pointPos, [pointPos[0], position[1]], SinColor, 3, "sinθ", "Right")
    cosLine  = Line( pointPos, [position[0], pointPos[1]], CosColor, 3, "cosθ", "Top")
    tanLine  = Line( pointPos, [position[0] + secante , position[1]], TanColor, 3, "tanθ", "Top")
    ctanLine = Line( pointPos, [position[0], + position[1]-cosecante], CtanColor, 3, "cotanθ", "Top")
    SecLine  = Line( position, [position[0] + secante , position[1]], SecColor, 3, "secθ", "Bottom")
    CscLine  = Line( position, [position[0]  , position[1] - cosecante], CscColor, 3, "cscθ", "Left")

    if pause==False:
        Xwave.insert(0, pointPos[1])
        Ywave.insert(0, pointPos[0])
        TanGraph.insert(0, tan_val)
        SecWave.insert(0, secante)
        CscWave.insert(0, cosecante*-1)

        if len(Xwave) > limit:
            Xwave.pop()
            Ywave.pop()
            TanGraph.pop()
            SecWave.pop()
            CscWave.pop()

    #draw waves
    if offsetWaves == False:
        waveOffset = 0

    else:
        waveOffset = radius
    previousTan = 0
    previousSec = 0
    previousCsc = 0

    for i in range(len(Xwave)):

        if showXwave:
            if i > 0:
                pygame.draw.line(screen, XwaveColor, (i+ position[0]+waveOffset, Xwave[i]),(i+ position[0]+waveOffset, Xwave[i-1]), strokeGraph)
                if projection:
                    pygame.draw.line(screen, XwaveColor, (position[0] - i -waveOffset, Xwave[i]),(position[0]-i-waveOffset, Xwave[i-1]), strokeGraph)

        if showYwave:
            if i > 0:
                pygame.draw.line(screen, YwaveColor, (Ywave[i], position[1] + waveOffset + i),(Ywave[i-1], position[1] + waveOffset + i), strokeGraph)
                if projection:
                    pygame.draw.line(screen, YwaveColor, (Ywave[i], position[1] - waveOffset - i),(Ywave[i-1], position[1] - waveOffset - i), strokeGraph)

        if showTanGraph:
            if i>0 and previousTan > -1000 and previousTan < 1000:
                pygame.draw.line(screen, TanGraphColor, (position[0]+i+waveOffset, TanGraph[i-1]+position[1]), (position[0]+i+waveOffset, TanGraph[i]+position[1]) ,strokeGraph)

            previousTan = TanGraph[i]

        if showSecFunction:
            if i>0 and previousSec > -1000 and previousSec < 1000:
                pygame.draw.line(screen, SecFunctionColor, (SecWave[i]+position[0], position[1]+i+waveOffset),(SecWave[i-1]+position[0], position[1]+i+waveOffset), strokeGraph)
            previousSec=SecWave[i]

        if showCscFunction:
            if i>0 and previousCsc > -1000 and previousCsc < 1000:
                pygame.draw.line(screen, CscFunctionColor, (position[0]+i+waveOffset, CscWave[i]+position[1]),(position[0]+i+waveOffset, CscWave[i-1]+position[1]), strokeGraph)

            previousCsc=CscWave[i]

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
        panel.Render(screen)
        CosText.Render(screen)
        SinText.Render(screen)
        TanText.Render(screen)
        CoText.Render(screen)
        SecText.Render(screen)
        CosecText.Render(screen)
        SinWaveText.Render(screen)
        CosWaveText.Render(screen)
        TanGraphText.Render(screen)
        SecFunctionText.Render(screen)
        CscFuncitonText.Render(screen)
        WOffsetText.Render(screen)
        AngleText.Render(screen)
        PressSpaceText.Render(screen)
        LineText.Render(screen)
        RadiusText.Render(screen)
        SpeedText.Render(screen)
        DarkText.Render(screen)
        ValuesText.Render(screen)
        projectionText.Render(screen)
        #toggle buttons
        showSin= SinToggle.Render(screen, clicked)
        showCos = CosToggle.Render(screen, clicked)
        showTan = TanToggle.Render(screen, clicked)
        showCtan = CoToggle.Render(screen, clicked)
        showSec = SecToggle.Render(screen, clicked)
        showCsc = CscToggle.Render(screen, clicked)
        showXwave = SinWaveToggle.Render(screen, clicked)
        showYwave = CosWaveToggle.Render(screen, clicked)
        offsetWaves = OffsetToggle.Render(screen, clicked)
        showTanGraph = TanGraphToggle.Render(screen, clicked)
        showSecFunction = SecFnToggle.Render(screen, clicked)
        showCscFunction = CscFnToggle.Render(screen, clicked)
        showTheta = AngleToggle.Render(screen, clicked)
        showLine = LineToggle.Render(screen, clicked)
        Dark = DarkToggle.Render(screen, clicked)
        projection = ProjectionToggle.Render(screen, clicked)
        #slider buttons
        radius = RadiusSlider.Render(screen)
        speed = speedSlider.Render(screen)

    else:
        UItoggle.Render(screen)

    if showValues:
        radius_value.text = "radius: " + str(radius)
        radius_value.Render(screen)

        Theta_value.text = "θ     : " + str(round(angle,2)) + "°"
        Theta_value.Render(screen)

        sin_value.text = "sinθ  : " + str(round(y, 2))
        sin_value.Render(screen)

        cos_value.text = "cosθ  : " + str(round(x, 2))
        cos_value.Render(screen)

        tan_value.text = "tanθ  : " + str(round(tan_val, 2))
        tan_value.Render(screen)

        ctn_value.text = "cotanθ: " + str(round(cotan_val, 2))
        ctn_value.Render(screen)

        sec_value.text = "secθ  : " + str(round(secante, 2))
        sec_value.Render(screen)

        csc_value.text = "cscθ  : " + str(round(cosecante, 2))
        csc_value.Render(screen)
    pygame.display.flip()

    if pause==False:
        angle += speed
        if angle >= 360:
            angle = 0.0001
    #UItoggle.fontSize = int( sin(angle/3) +24)
    clicked = False
pygame.quit()
sys.exit()
