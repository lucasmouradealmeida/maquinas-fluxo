from resources.velocidades_angulos_resource import VelocidadesAngulosResource
from resources.energias_vazao_rendimentos_resource import EnergiasResource
import numpy as np

def energias_vazao_rendimentos(
        input: VelocidadesAngulosResource, mi, Ep, d_ext, d_int, beta4, rho, mponto_f, k, n_m
    ) -> EnergiasResource:

    ypa_din = ((input.c5**2 - input.c4**2)/2)
    ypa_est = ((input.u5**2 - input.u4**2) / 2) + ((input.w4**2 - input.w5**2)/2)

    ypa_infinito = ypa_din + ypa_est

    ypa = mi * ypa_infinito

    y = ypa - Ep

    #Vazao volumetrica do ar
    area = ((d_ext/2)**2 - (d_int/2)**2)
    q_ponto = area * np.pi * input.c4 * np.cos(np.deg2rad(beta4))

    # Vaxao massica do ar
    m_ponto = rho * area * input.c4 * np.cos(np.deg2rad(beta4))

    # Potencia disponivel
    P = m_ponto * y

    # Energia perdida por fugas volumetricas
    Ef = mponto_f/m_ponto * ypa

    # Potencia consumida por atrito de disco
    Pa = k * rho * input.u4**3 * d_ext**2

    # Rendimento hidraulico
    n_h = y / ypa

    # Rendimento volumetrico
    n_v = m_ponto / (m_ponto + mponto_f)

    # Redimento de atrito de disco
    n_a = ((y + Ep) * (m_ponto + mponto_f)) / (((y + Ep) * (m_ponto + mponto_f)) + Pa)

    # Potencia interna
    Pi =  ((y - Ep) * (m_ponto + mponto_f)) + Pa

    # Rendimento interno
    n_i = P / Pi

    # Potencia de eixo 
    Pe = m_ponto * y * n_i * n_m

    # Grau de reacao real
    rho_real = ypa_est/y

    return EnergiasResource(
        ypa_din=ypa_din,
        ypa_est=ypa_est,
        ypa_infinito=ypa_infinito,
        y_pa=ypa,
        y=y,
        q_ponto=q_ponto,
        m_ponto=m_ponto,
        P=P,
        Ef=Ef,
        Pa=Pa,
        n_h=n_h,
        n_v=n_v,
        n_a=n_a,
        Pi=Pi,
        n_i=n_i,
        Pe=Pe,
        rho_real=rho_real
    )