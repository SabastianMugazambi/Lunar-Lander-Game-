# interfaces.py
# A module containing two interfaces for the lunar lander game.
#
# Please mess around with this program, have fun with this game!
#
# by Andy Exley
#

from graphics import *


class TextLanderInterface:
    """Text-based interface for lander game. Use this one for testing"""

    def show_info(self, lander):
        print ("Lander Status: Altitude %d, Velocity %d, Fuel %d" %
            (lander.get_altitude(), lander.get_velocity(), lander.get_fuel()))

    def get_thrust(self):
        amtstr = raw_input("Thrust amount? ")
        return int(amtstr)

    def show_crash(self):
        print "Crash! Oh noes!"

    def show_landing(self):
        print "Hooray, the Eagle has landed!"

    def close(self):
        print "Goodbye"

class GraphicLanderInterface:
    """GraphicLanderInterface class is a graphical interface
        for your lunar lander game"""

    def __init__(self):
        """Constructor that initializes the graphics window
        and shapes that we will use for drawing things"""

        # initialize window
        self.window = GraphWin("Lunar Lander Game", 300, 500)
        self.window.setBackground('black')
        # transform coordinates
        #drawing all the components of the space scene.
        self.buttonY = RectangleButton(Point(105,575), 50,50,"Thrust")
        self.buttonN = RectangleButton(Point(40,575),70,50, "No Thrust")
        self.button2 = RectangleButton(Point(160,575),50,50,"Thrust*2")
        self.button3 = RectangleButton(Point(215,575),50,50,"Thrust*3")

        self.updated = Text(Point(150,500), "String")
        self.Crush = Text(Point(150,300),"String")
        self.updated.setTextColor('blue')
        self.Crush.setTextColor('blue')
        self.window.setCoords(0, -10, 300, 600)

        self.surface_polygon = self.create_surface()
        self.surface_polygon.draw(self.window)
        self.buttonN.draw(self.window)
        self.buttonY.draw(self.window)
        self.button2.draw(self.window)
        self.button3.draw(self.window)
        self.lander_polygon = None
        self.sun = Circle(Point(40,400),50)
        self.earth = Circle(Point(200,350),30)
        self.earth.setFill('skyblue')
        self.earth.draw(self.window)
        self.sun.setFill('orange')
        self.sun.draw(self.window)


    def show_info(self, lander):
        """This method currently gets the lander info then draws it.
        That's it. Also displays the info onto the graphical window."""
        alt = lander.get_altitude()

        # if lander polygon is drawn, undraw it
        if self.lander_polygon:
            self.lander_polygon.undraw()
        self.lander_polygon = Polygon(Point(self.window.width / 2 - 10, alt),
                Point(self.window.width/2 - 3, alt+10 ),
                Point(self.window.width/2 + 3, alt+10 ),
                Point(self.window.width/2 + 10, alt))
        self.lander_polygon.setFill("blue")
        self.lander_polygon.draw(self.window)

        self.updated.setText(("Lander Status:\n Altitude %d, Velocity %d, Fuel %d" %
            (lander.get_altitude(), lander.get_velocity(), lander.get_fuel())))
        self.updated.draw(self.window)

    def get_thrust(self):
        """This method waits for a user's mouse click then returns 0 thrust
            amount. You'll want to fix this to avoid catastrophic incidents."""

        p = self.window.getMouse()

        #loops to check if user has clicked in the buttons and return the relative numbers of thrusts.
        if self.buttonN.clicked(p) == True:
            self.updated.undraw()
            return 0

        if self.buttonY.clicked(p) == True:
            self.updated.undraw()
            return 1
        if self.button2.clicked(p) == True:
            self.updated.undraw()
            return 2
        if self.button3.clicked(p) == True:
            self.updated.undraw()
            return 3

        return self.get_thrust()



    def show_crash(self):
        """Crash message... change this to graphical message"""
        self.Crush.setText("Crash! Oh noes!, Click to Close")
        #undrawing everything and adding a nice image of explosion.
        self.lander_polygon.undraw()
        self.surface_polygon.undraw()
        self.sun.undraw()
        self.earth.undraw()
        self.buttonY.undraw()
        self.buttonN.undraw()
        self.button2.undraw()
        self.button3.undraw()
        self.image = Image (Point(150,150),'explosion.gif')
        self.image.draw(self.window)
        self.Crush.draw(self.window)
        print "Crash! Oh noes!"
        self.window.getMouse()

    def show_landing(self):
        """Landing message... change this to graphical message"""
        self.Crush.setText("Hooray, the Eagle has landed! Click to close")
        #undrawing everything and adding a nice image of a smiley face.
        self.lander_polygon.undraw()
        self.surface_polygon.undraw()
        self.sun.undraw()
        self.earth.undraw()
        self.buttonY.undraw()
        self.buttonN.undraw()
        self.button2.undraw()
        self.button3.undraw()
        self.image = Image (Point(150,150),'happy.gif')
        self.image.draw(self.window)
        self.Crush.draw(self.window)

        print "Hooray, the Eagle has landed!"
        self.window.getMouse()

    def close(self):
        self.window.close()

    def create_surface(self):
        """Draws the surface of the moon"""
        rect = Oval(Point(5,-20),Point(310,0))
        rect.setFill("gray")
        return rect

class RectangleButton:
    """ This class is responsible for drawing all the buttons that were  used in the interface."""
    def __init__(self, center, width, height, text):
        w, h = width / 2.0, height / 2.0
        self.xmin, self.xmax = center.getX() - w, center.getX() + w
        self.ymin, self.ymax = center.getY() - h, center.getY() + h
        self.rect = Rectangle(Point(self.xmin, self.ymin),
                                Point(self.xmax, self.ymax))
        self.text = Text(center, text)
        self.text.setTextColor('blue')
        self.rect.setFill('red')

    def draw(self, window):
    #draws the rectangle button in the window.
        self.rect.draw(window)
        self.text.draw(window)

    def getLabel(self):
    #gets the text on the button
        return self.text.getText()

    def clicked(self, p):
        return (self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def undraw(self):
        self.rect.undraw()
        self.text.undraw()
