import numpy as np
import pygame
from astropy.constants import G, au
from main import WinWidth, WinHeight

def distance(point1, point2):
    # Calculate the difference vector between the points
    diff = point1 - point2
    # Calculate the magnitude of the difference vector using the dot product and square root operations
    return np.sqrt(np.dot(diff, diff))


def gravitational_force(planet1, planet2):
    # Calculate the distance between the two planets
    distance = ((planet1.x - planet2.x)**2 + (planet1.y - planet2.y)**2)**0.5
    # Calculate the gravitational force
    force = G.value * (planet1.mass * planet2.mass) / (distance**2)

    return force

   
class Planet:
    scale = 250000 / au.value
    def __init__(self, name, x, y, mass, radius, velocity, color):
        self.name = name
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.velocity = velocity
        self.color = color

    def __str__(self):
        return f"{self.name}: Planet at position ({self.x}, {self.y}) with mass {self.mass} kg and radius {self.radius} km"

    def update_position(self, force, time_step, current_x, current_y):
        # Calculate acceleration based on the provided force and mass
        acceleration_x = force[0] / self.mass
        acceleration_y = force[1] / self.mass

        # Update position using the equations of motion
        self.x = current_x + (self.x - current_x) + acceleration_x * (time_step**2)
        self.y = current_y + (self.y - current_y) + acceleration_y * (time_step**2)

    def draw(self, win):
        # update position to the center of the window and scale it 
        dx = self.x * self.scale/3000 + (WinWidth / 2)
        dy = self.y * self.scale/3000 + (WinHeight / 2)
        pygame.draw.circle(win, self.color, (dx, dy), self.radius*self.scale)

class Star(Planet):
    scale = 2500 / au.value

sun = Star("Sun", x=0, y=0, mass=1988500e24, radius=695700*1000, velocity=(0,0), color=(255, 165, 0))
mercury = Planet("Mercury", x=57.909e9, y=0, mass=0.33010e24, radius=2440.5*1000, velocity=(0, 47.36*1000), color=(114, 47, 55))
venus = Planet("Venus", 0.72e11, 0, 4.8675e24, 6051.8*1000, (0, 35020), (3,217,45))
#earth = Planet("Earth", 1.496e11, 0, 5.972e24, 6371, (0, 29783))
#mars = Planet("Mars", 2.28e11, 0, 6.39e23, 3389.5, (0, 24007))

CelestialObjects = [sun, mercury, venus]