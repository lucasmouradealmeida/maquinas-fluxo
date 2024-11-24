from services.velocidades_angulos import velocidades_angulos
from services.energias_vazao_rendimentos import energias_vazao_rendimentos

# Rotação do motor
n = 1800 # rpm

# Diametro da hélice
d_ext = 0.5 # m
d_int = 0.3 # m

# Angulos dos tringulos de velocidade
# Entrada
alpha4 = 60 # graus
beta4 = 30 # graus

# Saida
beta5 = 44.3 # graus

# Fator de deficiencia de potencia das pas
mi = 0.88

# Perdas Hidraulicas
Ep = 28 # J/kg

# Densidade do ar
rho = 1.1 # kg/m³

# Fuga de vazao massica
mponto_f = 0.03 # kg/s

# Coeficiente adimensional
k = 0.003

# Rendimento mecanico
n_m = 0.95

# Serviço de determinação do triângulo de velocidades
result_velocidades = velocidades_angulos(n, d_ext, d_int, alpha4, beta4, beta5)
print(result_velocidades)

# Serviço de determinação das energias
result_energias = energias_vazao_rendimentos(result_velocidades,mi, Ep, d_ext, d_int, beta4, rho, mponto_f, k, n_m)
print(result_energias)








