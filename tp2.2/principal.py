import distribuciones
import graficas
import numpy as np
import pruebas
import scipy.stats as stats

uniforme = []
exponencial = []
normal = []
gamma = []
pascal = []
binomial = []
hipergeometrica = []
poisson = []

for i in range(1000):
    #uniforme.append(distribuciones.distribucion_uniforme(5,15))
    #exponencial.append(distribuciones.distribucion_exponencial(0.5))
    #gamma.append(distribuciones.distribucion_gamma(5,1))
    #normal.append(distribuciones.distribucion_normal(0.5,0.2))
    #pascal.append(distribuciones.distribucion_pascal(5,0.4))
    #binomial.append(distribuciones.distribucion_binomial(20,0.5))
    #hipergeometrica.append(distribuciones.distribucion_hipergeometrica(900,100,0.4))
    #poisson.append(distribuciones.distribucion_poisson(10))
    pass

#Prueba para ver si la distribucion funciona
#UNIFORME
#graficas.histograma(uniforme)
#print(np.mean(uniforme))
#print(pruebas.Kolmogorov(uniforme, 0.05))
#print(pruebas.ChiCuadrado(uniforme, 0.95, 9))

#EXPONENCIAL
#graficas.histograma(exponencial)
#pruebas.Anderson(exponencial,'expon')

#NORMAL
#normalNumpy = np.random.normal(size=1000)
#print(stats.kstest(normal,'norm'))
#graficas.histograma(normal)
#print(pruebas.Kolmogorov(normal, 0.05))
#print(pruebas.ChiCuadrado(normal, 0.95, 9))
#pruebas.Anderson(normal,'norm')

#GAMMA
#graficas.histograma(gamma)
#print(pruebas.Kolmogorov(gamma, 0.05))
#print(pruebas.ChiCuadrado(gamma, 0.95, 9))

#PASCAL
#graficas.histograma(pascal)

#BINOMIAL
#graficas.histograma(binomial)

#HIPERGROMETRICA
#graficas.histograma(hipergeometrica)

#POISSON
#graficas.histograma(poisson)

