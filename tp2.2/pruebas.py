from scipy.stats import kstest
import scipy.stats as stats
import numpy as np
from scipy.stats import ksone
from scipy.stats import norm
from math import sqrt
from math import floor
from scipy.stats import chi2
from scipy.stats import anderson

def ChiCuadrado(numerosAleatorios,q,df):
   numeros = numerosAleatorios
   frec_obt_int = np.histogram(numeros, bins=10)  # Frecuencia en cada intervalo
   # Frecuencia en cada rango
   suma_epic = 0
   arreglo_suma_epic = []
   cont = len(numeros) / 10
   # 3. a cada intervalo le aplico la siguiente ecuacion (Ef - Ee)^2/Ee y hago la sumatoria
   for i in range(10):
       calculo = ((frec_obt_int[0][i - 1] - cont) ** 2) / cont
       arreglo_suma_epic.append(calculo)
   suma_epic = sum(arreglo_suma_epic)
   # 5. comparo en tabla de chi cuadrado con un nivel de confianza
   # Se hace con el valor suma epic
   # Si suma_epic es mayor que el valor por tabla, se rechaza ( no es uniforme)

   #Obtengo el valor de l tabla para
   #q = intervalo de confianza
   #df  = grados de libertad
   chi_cuadrado_tabla = stats.chi2.ppf(q=q, df=df)


   if suma_epic < chi_cuadrado_tabla:
       resultado = True
   else:
       resultado = False

   return  resultado, arreglo_suma_epic, suma_epic, chi_cuadrado_tabla

def Kolmogorov(numeros, alpha):

#Ordenar los numeros en forma ascendente
    num_ordenados = sorted(numeros)
    tamaño = len(num_ordenados)

#Calculo D+ Y D-
    D_Mas = max(((i+1)/tamaño - num_ordenados[i]) for i in range(tamaño))
    D_Menos = min((num_ordenados[i] - (i-1)/tamaño) for i in range(tamaño))

#Obtengo el mas grande
    D = max(abs(D_Mas) ,abs(D_Menos))

#Busco el valor critico de la tabla de kolmogorov para ese nivel de significancia y lo comparo con D
#Si D es menor que el valor critico puedo decir que los datos pertenecen a una distribucion uniforme
#Para buscar los datos uso la libreria de scipy
    valor_critico = (ksone.pdf(alpha/2, tamaño))
    if D < valor_critico:
        resultado = True
    else:
        resultado = False

    return resultado, D_Mas, D_Menos, valor_critico

def Anderson(array_distribucion,tipo):
    result = anderson(array_distribucion, tipo)
    print('Statistic: %.3f' % result.statistic)
    p = 0
    for i in range(len(result.critical_values)):
        sl, cv = result.significance_level[i], result.critical_values[i]
        if result.statistic < result.critical_values[i]:
            print('%.3f: %.3f, (Se acepta H0)' % (sl, cv))
        else:
            print('%.3f: %.3f, (Se rechaza H0)' % (sl, cv))

