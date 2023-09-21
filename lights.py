import numpy as np

DIR_LIGHT = 0
POINT_LIGHT = 1
AMBIENT_LIGHT = 2

class DirectionalLight(object):
    def __init__(self, direction = (0,-1,0), intensity = 1, color = (1,1,1)):
        self.direction = direction / np.linalg.norm(direction)
        self.intensity = intensity
        self.color = color
        self.lightType = DIR_LIGHT

class AmbientLight(object):
    def __init__(self, intensity = 0.1, color = (1,1,1)):
        self.intensity = intensity
        self.color = color
        self.lightType = AMBIENT_LIGHT

class PointLight(object):
    def __init__(self, point, constant=1.0, linear=0.1, quad=0.05, color=(1, 1, 1)):
        self.point = point
        self.constant = constant
        self.linear = linear
        self.quad = quad
        self.color = color
        self.lightType = POINT_LIGHT
