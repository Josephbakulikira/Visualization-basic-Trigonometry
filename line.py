import pygame

class Line:
    def __init__(self, pointA, pointB, color, stroke=5, text=None, textPosition="Top"):
        self.pointA = [int(i) for i in pointA]
        self.pointB = [int(i) for i in pointB]
        self.color = color
        self.text = text
        self.textPosition = textPosition
        self.stroke = stroke
        self.font = 'freesansbold.ttf'
        self.fontSize = 18
        self.textColor = color
    def Show(self, screen):
        #get mid point of a segment
        x = (self.pointA[0] + self.pointB[0])//2
        y = (self.pointA[1] + self.pointB[1])//2

        if self.textPosition == "Top":
            y -= self.stroke * 5
        elif self.textPosition == "Bottom":
            y += self.stroke * 5
        elif self.textPosition == "Right":
            x += self.stroke * 5
        else:
            x -= self.stroke * 5
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text, True, self.textColor)
        textRect = text.get_rect()
        textRect.center = (x, y)
        try:
          pygame.draw.line(screen, self.color, self.pointA, self.pointB, self.stroke)
          screen.blit(text, textRect)
        except Exception as e:
          print("An exception occurred: ", e)
