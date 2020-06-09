import distribuciones
import graficas
import numpy as np
import pruebas
import scipy.stats as stats
from scipy.stats.contingency import expected_freq
import matplotlib.pyplot as plt
from scipy.stats import chisquare

#DISTRIBUCIONES
"""
uniforme = distribuciones.distribucion_uniforme(0,20)
exponencial = distribuciones.distribucion_exponencial(0.5)
gamma = distribuciones.distribucion_gamma(5,1)
normal = distribuciones.distribucion_normal(10,20)
pascal = distribuciones.distribucion_pascal(5,0.4)
binomial = distribuciones.distribucion_binomial(20,0.5)
hipergeometrica = distribuciones.distribucion_hipergeometrica(5000000,500,0.4)
poisson = distribuciones.distribucion_poisson(10)
empirica = distribuciones.distribucion_empirica()

#GRAFICAS
graficas.histograma(uniforme)
graficas.histograma(exponencial)
graficas.histograma(gamma)
graficas.histograma(normal)
graficas.histograma(pascal)
graficas.histograma(binomial)
graficas.histograma(hipergeometrica)
graficas.histograma(poisson)
graficas.histograma(empirica)

#PRUEBAS
#print(pruebas.Kolmogorov(uniforme, 0.05))
#pruebas.Anderson(exponencial,'expon')
#pruebas.Anderson(normal,'norm') 
"""

#poisson = distribuciones.distribucion_poisson(10)
#print(np.mean(poisson))
#print(np.var(poisson))

#binomial = distribuciones.distribucion_binomial(20,0.5)
#print(np.mean(binomial))
#print(np.var(binomial))

#hipergeometrica = distribuciones.distribucion_hipergeometrica(5000000,500,0.4)
#print(np.mean(hipergeometrica))
#print(np.var(hipergeometrica))

#gamma = distribuciones.distribucion_gamma(5,1)
#print(np.mean(gamma))
#print(np.var(gamma))

#NO FUNCIONANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
#empirica = distribuciones.distribucion_empirica()
#print(np.mean(empirica))
#print(np.var(empirica))

#pascal = distribuciones.distribucion_pascal(5,0.2)
#print(np.mean(pascal))
#print(np.var(pascal))
