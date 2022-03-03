import math

def movimentHarmonic(amplitud, freq, temps, faseInicial=0):
    omega = 2 * math.pi * freq 

    x = amplitud * math.sin(omega * temps + faseInicial)
    v = amplitud * omega * math.cos(omega * temps + faseInicial)
    a = amplitud * omega*omega * math.sin(omega * temps + faseInicial) * -1

    return [x, v, a]

def maxMovimentHarmonic(amplitud, freq, temps, faseInicial=0):
    omega = 2 * math.pi * freq

    v = amplitud * omega
    a = omega * omega * amplitud

    return [v, a]
