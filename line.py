import pygame

class Line:
    def __init__(self, pointA, pointB, color, stroke=5, text=None, textPosition=None):
        self.pointA = [int(i) for i in pointA]
        self.pointB = [int(i) for i in pointB]
        self.color = color
        self.text = text
        self.textPosition = textPosition
        self.stroke = stroke

    def Show(self, screen):
        try:
          pygame.draw.line(screen, self.color, self.pointA, self.pointB, self.stroke)
        except Exception as e:
          print("An exception occurred: ", e)
        
