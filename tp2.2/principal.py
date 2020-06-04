import distribuciones
import graficas
import numpy as np
import pruebas

uniforme = []
exponencial = []

for i in range(1000):
    uniforme.append(distribuciones.distribucion_uniforme(5,15))
    #exponencial.append(distribuciones.distribucion_exponencial(0.5))



#Prueba para ver si la distribucion funciona
#UNIFORME
#print(np.mean(uniforme))
print(pruebas.Kolmogorov(uniforme, 0.05))

#EXPONENCIAL
#graficas.histograma(exponencial)
#pruebas.Anderson(exponencial)
