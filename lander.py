#-------------------------------------------------------------------------------
# Author:      Sabastian Mugazambi
# Name:  Simulation of the lunar Lander game.
# Purpose:To get comfortable with writing classes and making calls to the
#         methods of the classes
# Created:     12/05/2014
#-------------------------------------------------------------------------------
import graphics
from interfaces import *

class LunarLander:
    """This class will represent the ship that is being manipulated to land"""
    def __init__(self, alt, vel, fuel):
        """initializing the variables for the parameters taken by the constructor."""
        self.alt = alt
        self.vel = vel
        self.fuel = fuel


    def get_altitude(self):
        """Stores the value of the current alttidude."""
        return self.alt


    def get_velocity(self):
        """Stores the value of the current velocity."""
        return self.vel


    def get_fuel(self):
        """Stores the value of the current amount of fuel."""
        return self.fuel

    def update(self, thrust_amount):
        """Reduces the amount of fuel by the number of thrust entered and increases
        the velocity inrelation to the number of thrusts.Dertermines the new altitude
         of the lander and checks if they have landed or still trying to land."""
         #compares the thrust_amount to the available fuel because one cen not use fuel he/she does not have.
        if thrust_amount <= self.fuel :
            self.fuel = (self.get_fuel()) - (thrust_amount)

        else:
            #reduces the number of thrusts to the maximum possible thrust according to fuel and sets the fuel to zero.
            thrust_amount = self.fuel
            self.fuel = 0

        self.vel = (self.get_velocity() + thrust_amount*4)-2
        self.alt = self.get_altitude() + self.get_velocity()


def testLander():
    """Tests the class LunarLander to see if its working properly by passing
    in preset parameters and caling it in the main.Creates the instance lander and works with it. """
    lander = LunarLander(200,0,30)
    lander.update(0)
    print lander.get_altitude()

    #testing if the Lander lands when they are supposed to or remain flying if the altitude is greater than zero.
    if lander.alt > 0:
        print "Still in air"
    else:
        print "Crashed or Landed"



class LanderGame:
    """This class will represent the lander/the player while calling to TextLanderInterface methods."""

    def __init__(self):
        """Initializing the instance variables for the LunarLander class and the TextLanderInterface class"""
        self.lander = LunarLander(200,0,30)
        self.interface = TextLanderInterface()


    def play(self):
        """Checks if the altitude is greater than zero then loops, asking the user
        the thrust amount using TextLanderInterface methods.Displays the current
        state of the ship interms of altitude, velocity and fuel. Updates the state
        of the ship in relation to the thrust entered by the user."""

        while self.lander.alt > 0:
            self.interface.show_info(self.lander)
            self.lander.update(self.interface.get_thrust())

        #Checking if the lunar lander has crashed or landed by checking for the velocity after altitude falls below zero.
        if self.lander.vel > -10:
            self.interface.show_landing()
        else:
            self.interface.show_crash()
        self.interface.close()


def main():
    """Creates an instance of the LanderGame class and uses the play method on it
    so as to start paying the game. It also includes the call to the testing function."""
##       testLander()
    start_game = LanderGame()
    start_game.play()







if __name__ == '__main__':
    main()
