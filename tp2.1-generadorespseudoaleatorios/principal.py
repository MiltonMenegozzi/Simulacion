import generadores
import pruebas
import graficas
from math import pow
import numpy as np



#generadores.media_de_los_cuadrados(1931,10)
#numerosGCL = generadores.generadorgcl(1234,134775813, 1, pow(2, 32),1000)
#numerosNumpy = generadores.generarNumpy(1000)

#Prueba kolmogorov
#print(pruebas.Kolmogorov(numeros, 0.05)) # Numeros, alpha

#Prueba ChiCuadrado
#print(pruebas.ChiCuadrado(numeros, 0.95, 9)) #Numeros, int confianza, grados libertad

#Prueba Paridad
#resultado_paridad_Numpy = pruebas.Paridad(numerosNumpy)
#resultados_paridad_GCL = pruebas.Paridad(numerosGCL)
#graficas.graficoCircular(resultado_paridad_Numpy[0], resultado_paridad_Numpy[1],'Generador Numpy')
#graficas.graficoCircular(resultados_paridad_GCL[0], resultados_paridad_GCL[1], 'Generador GCL')

#Prueba Corrida
#print(pruebas.PruenaDeCorrida(numerosNumpy, 0.05))
#print(pruebas.PruenaDeCorrida(numerosGCL, 0.05))

