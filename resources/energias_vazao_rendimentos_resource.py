from pydantic import BaseModel


class EnergiasResource(BaseModel):
    ypa_din: float
    ypa_est: float
    ypa_infinito: float
    y_pa: float
    y : float
    q_ponto: float
    m_ponto: float
    P: float
    Ef: float
    Pa: float
    n_h: float
    n_v: float
    n_a: float
    Pi: float
    n_i: float
    Pe: float
    rho_real: float