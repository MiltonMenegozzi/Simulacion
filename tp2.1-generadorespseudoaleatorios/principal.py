import generadores
import pruebas
import graficas
from math import pow
import numpy as np



#generadores.media_de_los_cuadrados(1931,10)
numerosGCL = generadores.generadorgcl(25214903917,0.5, 11, pow(2, 48),1000)
numerosNumpy = generadores.generarNumpy(1000)

#print(pruebas.Kolmogorov(numeros, 0.05)) # Numeros, alpha

#print(pruebas.ChiCuadrado(numeros, 0.95, 9)) #Numeros, int confianza, grados libertad

resultado_paridad_Numpy = pruebas.Paridad(numerosNumpy)
resultados_paridad_GCL = pruebas.Paridad(numerosGCL)
graficas.graficoCircular(resultado_paridad_Numpy[0], resultado_paridad_Numpy[1],'Generador Numpy')
graficas.graficoCircular(resultados_paridad_GCL[0], resultados_paridad_GCL[1], 'Generador GCL')
