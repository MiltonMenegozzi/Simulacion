import distribuciones
import graficas
import numpy as np
import pruebas
import scipy.stats as stats

uniforme = []
exponencial = []
normal = []

for i in range(1000):
    uniforme.append(distribuciones.distribucion_uniforme(5,15))
    #exponencial.append(distribuciones.distribucion_exponencial(0.5))


for i in range(1000):
    normal.append(distribuciones.distribucion_normal(0.5,0.2))

#Prueba para ver si la distribucion funciona
#UNIFORME
#print(np.mean(uniforme))
print(pruebas.Kolmogorov(uniforme, 0.05))

#EXPONENCIAL
#graficas.histograma(exponencial)
#pruebas.Anderson(exponencial)


#NORMAL
graficas.histograma(normal)
print(stats.kstest(normal,'norm'))