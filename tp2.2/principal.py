import distribuciones
import graficas
import numpy as np
import pruebas
import scipy.stats as stats



""""DISTRIBUCIONES"""
#uniforme = distribuciones.distribucion_uniforme(0,20)
#exponencial = distribuciones.distribucion_exponencial(0.5)
gamma = distribuciones.distribucion_gamma(5,1)
#normal = distribuciones.distribucion_normal(0.5,0.2)
#pascal = distribuciones.distribucion_pascal(5,0.4)
#binomial = distribuciones.distribucion_binomial(20,0.5)
#hipergeometrica = distribuciones.distribucion_hipergeometrica(40,11,11)
#poisson = distribuciones.distribucion_poisson(10)
#empirica = distribuciones.distribucion_empirica()


#Prueba para ver si la distribucion funciona



#print(pruebas.ChiCuadrado(uniforme, 0.95, 9))

#EXPONENCIAL

#NORMAL
#normalNumpy = np.random.normal(size=1000)
#print(stats.kstest(normal,'norm'))
#print(pruebas.Kolmogorov(normal, 0.05))
#print(pruebas.ChiCuadrado(normal, 0.95, 9))
#pruebas.Anderson(normal,'norm')

#GAMMA
#print(pruebas.Kolmogorov(gamma, 0.05))
#print(pruebas.ChiCuadrado(gamma, 0.95, 9))


"""PRUEBAS"""
#print(pruebas.Kolmogorov(uniforme, 0.05))
#pruebas.Anderson(exponencial,'expon')
print(pruebas.KolmogorovScipy(gamma))

"""GRAFICAS"""
#graficas.histograma(uniforme)
#graficas.histograma(exponencial)
#graficas.histograma(gamma)
#graficas.histograma(normal)
#graficas.histograma(pascal)
#graficas.histograma(binomial)
#graficas.histograma(hipergeometrica)
#graficas.histograma(poisson)
#graficas.histograma(empirica)
