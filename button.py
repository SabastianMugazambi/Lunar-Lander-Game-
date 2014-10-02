# button class example

from graphics import *

class RectangleButton:
    def __init__(self, center, width, height, text):
        w, h = width / 2.0, height / 2.0
        self.xmin, self.xmax = center.getX() - w, center.getX() + w
        self.ymin, self.ymax = center.getY() - h, center.getY() + h
        self.rect = Rectangle(Point(self.xmin, self.ymin),
                                Point(self.xmax, self.ymax))
        self.text = Text(center, text)

    def draw(self, window):
        self.rect.draw(window)
        self.rect.setFill('green')
        self.text.draw(window)

    def getLabel(self):
        return self.text.getText()

    def clicked(self, p):
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)
