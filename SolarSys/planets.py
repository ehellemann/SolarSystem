import units
import numpy as np

def distance(point1, point2):
    # Calculate the difference vector between the points
    diff = point1 - point2
    
    # Calculate the magnitude of the difference vector using the dot product and square root operations
    return np.sqrt(np.dot(diff, diff))
    
def gravitational_force(planet1, planet2):
    G = 6.67430e-11  # Gravitational constant in N*m^2/kg^2

    # Calculate the distance between the two planets
    distance = ((planet1.x - planet2.x)**2 + (planet1.y - planet2.y)**2)**0.5

    # Calculate the gravitational force
    force = G * (planet1.mass * planet2.mass) / (distance**2)

    return force
    
class Planet:
    def __init__(self, name, x, y, mass, radius, velocity):
        self.name = name
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.velocity = velocity

    def __str__(self):
        return f"{self.name}: Planet at position ({self.x}, {self.y}) with mass {self.mass} kg and radius {self.radius} km"

    def update_position(self, force, time_step, current_x, current_y):
        # Calculate acceleration based on the provided force and mass
        acceleration_x = force[0] / self.mass
        acceleration_y = force[1] / self.mass

        # Update position using the equations of motion
        self.x = current_x + (self.x - current_x) + acceleration_x * (time_step**2)
        self.y = current_y + (self.y - current_y) + acceleration_y * (time_step**2)

