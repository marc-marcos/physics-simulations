import math

def movimentHarmonic(amplitud, freq, temps):
    omega = 2 * math.pi * freq 

    x = amplitud * math.sin(omega * temps)

    v = amplitud * omega * math.cos(omega * temps)

    a = amplitud * omega*omega * math.sin(omega * temps) * -1

    return [x, v, a]
