import math

def calcPend(radius, t, phi0):
    time = 2*math.pi * math.sqrt(radius / 9.81)
    omega = (2*math.pi)/time

    phi = omega*t + phi0

    return [radius*math.sin(phi), radius*math.cos(phi)]
