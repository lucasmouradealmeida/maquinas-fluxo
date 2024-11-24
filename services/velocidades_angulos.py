import numpy as np
from resources.velocidades_angulos_resource import VelocidadesAngulosResource

def velocidades_angulos(n, d1, d2, alpha4, beta4, beta5) -> VelocidadesAngulosResource:
    # Velocidade tangecial
    vt = (np.pi * n * (d1 + d2)/2) / 60

    # Velocidade tangencial de entrada
    u4 = vt

    # Velocidade tangencial de saída
    u5 = vt

    # Velocidade absoluta na entrada
    c4 = np.cos(np.deg2rad(alpha4)) * vt

    # Velocidade relativda na entrada
    w4 = np.sin(np.deg2rad(alpha4)) * vt

    #Equacao da continuidade
    # Q4 = Q5 -> Cm4 = Cm5 = Cm
    cm = np.sin(np.deg2rad(beta4)) * w4

    # Velocidade relativa na saída
    w5 = cm / np.sin(np.deg2rad(beta5))

    # Velocidade absoluta na saída (teorma dos cossenos)
    c5 = np.sqrt(w5**2 + u5**2 - 2 * w5 * u5 * np.cos(np.deg2rad(beta5)))

    # Angulo alpha5 pelo teorema dos senos
    alpha5 = np.rad2deg(np.arcsin(w5 * np.sin(np.deg2rad(beta5)) / c5))

    cu4 = np.cos(np.deg2rad(alpha4)) * c4
    cu5 = np.cos(np.deg2rad(alpha5)) * c5


    return VelocidadesAngulosResource(
        u4 = u4,
        u5 = u5,
        w4 = w4,
        w5 = w5,
        c4 = c4,
        c5 = c5,
        alpha5 = alpha5,
        cu4 = cu4,
        cu5 = cu5
    )