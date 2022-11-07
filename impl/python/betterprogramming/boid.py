from p5 import setup, draw, size, background, run

class Boid():

    def __init__(self, x, y, width, height):
        self.position = Vector(x, y)