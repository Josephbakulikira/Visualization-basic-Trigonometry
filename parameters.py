from ui import *

#circle
radius = 200
circleStroke = 3
angleArc = 100

waveOffset = radius
temp = waveOffset

# toggles
Dark = True
showAxis = True
showPoint = True
showLine = True
showOrigin = True
showCos = True
showSin = True
showTan = True
showCtan = True
showSec = True
showCsc = True
showTheta = False
showXwave = True
showYwave = True
showUI = False
offsetWaves = True
pause = False
# ui parameters

panel = Panel( position = (Width-380, 80), w= 360, h= 800, color=(0, 0, 0), alpha=100)

UItoggle = TextUI("Press 'SPACE' to show parameter panel", (Width-280, 120), (155, 120, 255))
UItoggle.fontSize = 23

SinText = TextUI(  "Sin :",       (Width-350, 180), (255, 255, 255), "topleft")
CosText = TextUI(  "Cos :",       (Width-350, 220), (255, 255, 255), "topleft")
TanText = TextUI(  "Tangent :",   (Width-350, 260), (255, 255, 255), "topleft")
CoText = TextUI(   "Cotangent :", (Width-350, 300), (255, 255, 255), "topleft")
SecText = TextUI(  "Secante :",   (Width-350, 340), (255, 255, 255), "topleft")
CosecText = TextUI("cosecante :", (Width-350, 380), (255, 255, 255), "topleft")
SinWaveText = TextUI("SinWave :",     (Width-350, 420), (255, 255, 255), "topleft")
CosWaveText = TextUI("CosineWave :",  (Width-350, 460), (255, 255, 255), "topleft")
WOffsetText = TextUI("Offset Waves :",(Width-350, 500), (255, 255, 255), "topleft")
AngleText = TextUI("Angle :",         (Width-350, 540), (255, 255, 255), "topleft")
LineText = TextUI("Radius Line :",         (Width-350, 580), (255, 255, 255), "topleft")
PressSpaceText = TextUI("Press 'P' To Pause ", (Width-200, 650), (135, 120, 205), "center")
RadiusText = TextUI("Radius :", (Width-350, 700), (255, 255, 255), "topleft")
SpeedText = TextUI("speed :", (Width-350, 750), (255, 255, 255), "topleft")
DarkText = TextUI("Dark Theme :", (Width-350, 820), (255, 255, 255), "topleft")

#toggles
SinToggle = ToggleButton((Width-200, 180), 20, 20, showSin)
CosToggle = ToggleButton((Width-200, 220), 20, 20, showCos)
TanToggle = ToggleButton((Width-200, 260), 20, 20, showTan)
CoToggle  = ToggleButton((Width-200, 300), 20, 20, showCtan)
SecToggle = ToggleButton((Width-200, 340), 20, 20, showSec)
CscToggle = ToggleButton((Width-200, 380), 20, 20, showCsc)
SinWaveToggle = ToggleButton((Width-200, 420), 20, 20, showXwave)
CosWaveToggle = ToggleButton((Width-200, 460), 20, 20, showYwave)
OffsetToggle =  ToggleButton((Width-200, 500), 20, 20, offsetWaves)
AngleToggle =   ToggleButton((Width-200, 540), 20, 20, showTheta)
LineToggle =    ToggleButton((Width-200, 580), 20, 20, showLine)
DarkToggle =    ToggleButton((Width-200, 820), 20, 20, Dark)

RadiusSlider = Slider(Width-250, 705, radius, 50, 600, 200, 10)
speedSlider = Slider(Width-250, 755, speed, 50, 600, 200, 10, 5)
