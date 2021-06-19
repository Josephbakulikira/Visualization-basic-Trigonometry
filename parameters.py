from ui import *

#circle
radius = 200
circleStroke = 3
angleArc = 100

waveOffset = radius
temp = waveOffset

# toggles
Dark = True
projection = False
showAxis = True
showPoint = True
showLine = True
showOrigin = True
showCos = True
showSin = True
showTan = False
showCtan = False
showSec = False
showCsc = False
showTheta = False
showXwave = False
showYwave = False
showTanGraph = False
showSecFunction = False
showCscFunction = False
showValues = False
showUI = False
offsetWaves = False
pause = False
# ui parameters

panel = Panel( position = (Width-380, 50), w= 360, h= 1000, color=(0, 0, 0), alpha=100)

UItoggle = TextUI("Press 'SPACE' to show parameter panel", (Width-280, 120), (55, 220, 55))
UItoggle.fontSize = 18

SinText = TextUI(  "Sin :",       (Width-350, 100), (255, 255, 255), "topleft")
CosText = TextUI(  "Cos :",       (Width-350, 140), (255, 255, 255), "topleft")
TanText = TextUI(  "Tangent :",   (Width-350, 180), (255, 255, 255), "topleft")
CoText = TextUI(   "Cotangent :", (Width-350, 220), (255, 255, 255), "topleft")
SecText = TextUI(  "Secante :",   (Width-350, 260), (255, 255, 255), "topleft")
CosecText = TextUI("cosecante :", (Width-350, 300), (255, 255, 255), "topleft")
SinWaveText = TextUI("SinWave :",     (Width-350, 340), (255, 255, 255), "topleft")
CosWaveText = TextUI("CosineWave :",  (Width-350, 380), (255, 255, 255), "topleft")
TanGraphText = TextUI("Tan Graph :", (Width-350, 420), (255, 255, 255), "topleft")
SecFunctionText = TextUI("Sec fn :", (Width-350, 460), (255, 255, 255), "topleft")
CscFuncitonText = TextUI("Csc fn :", (Width-350, 500), (255, 255, 255), "topleft")
WOffsetText = TextUI("Offset Waves :",(Width-350, 540), (255, 255, 255), "topleft")
AngleText = TextUI("θ :",         (Width-350, 580), (255, 255, 255), "topleft")
LineText = TextUI("Radius Line :",         (Width-350, 620), (255, 255, 255), "topleft")
PressSpaceText = TextUI("Press 'P' To Pause ", (Width-200, 700), (135, 120, 205), "center")
RadiusText = TextUI("Radius :", (Width-350, 750), (255, 255, 255), "topleft")
SpeedText = TextUI("speed :", (Width-350, 800), (255, 255, 255), "topleft")


#ValuesText
radius_value = TextUI("radius: 0", (100, 130), (255, 255, 255), "topleft")
Theta_value=TextUI("θ     : 0", (100, 160), (255, 255, 255), "topleft")
sin_value = TextUI("sinθ  : 0", (100, 190), (255, 255, 255), "topleft")
cos_value = TextUI("cosθ  : 0", (100, 220), (255, 255, 255), "topleft")
tan_value = TextUI("tanθ  : 0", (100, 250), (255, 255, 255), "topleft")
ctn_value = TextUI("cotanθ: 0", (100, 280), (255, 255, 255), "topleft")
sec_value = TextUI("secθ  : 0", (100, 310), (255, 255, 255), "topleft")
csc_value = TextUI("cscθ  : 0", (100, 340), (255, 255, 255), "topleft")

DarkText = TextUI("Dark Theme :", (Width-350, 970), (255, 255, 255), "topleft")
ValuesText = TextUI("Press 'S' to show values", (Width-200, 860), (135, 120, 205), "center")
projectionText = TextUI("Projection :", (Width-350, 920), (255, 255, 255), "topleft")
#toggles
SinToggle = ToggleButton((Width-200, 100), 20, 20, showSin)
CosToggle = ToggleButton((Width-200, 140), 20, 20, showCos)
TanToggle = ToggleButton((Width-200, 180), 20, 20, showTan)
CoToggle  = ToggleButton((Width-200, 220), 20, 20, showCtan)
SecToggle = ToggleButton((Width-200, 260), 20, 20, showSec)
CscToggle = ToggleButton((Width-200, 300), 20, 20, showCsc)
SinWaveToggle = ToggleButton((Width-200, 340), 20, 20, showXwave)
CosWaveToggle = ToggleButton((Width-200, 380), 20, 20, showYwave)
TanGraphToggle = ToggleButton((Width-200, 420), 20, 20, showTanGraph)
SecFnToggle = ToggleButton((Width-200, 460), 20, 20, showSecFunction)
CscFnToggle = ToggleButton((Width-200, 500), 20, 20, showCscFunction)

OffsetToggle =  ToggleButton((Width-200, 540), 20, 20, offsetWaves)
AngleToggle =   ToggleButton((Width-200, 580), 20, 20, showTheta)
LineToggle =    ToggleButton((Width-200, 620), 20, 20, showLine)
DarkToggle =    ToggleButton((Width-200, 970), 20, 20, Dark)
ProjectionToggle = ToggleButton((Width-200, 920), 20, 20, projection)


RadiusSlider = Slider(Width-250, 755, radius, 50, 600, 200, 10)
speedSlider = Slider(Width-250, 805, speed, 50, 600, 200, 10, 5)
