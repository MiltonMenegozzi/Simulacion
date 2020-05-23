import numpy as np
import matplotlib.pyplot as plt

def generarNumeroAleatorios():
   listaAleatorios = []
   for i in range(100):
       listaAleatorios.append(np.random.randint(0,37))
   return listaAleatorios


def calcularColor(numero):
  #ROJO DEVUELVE TRUE
  if numero in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
      return True
  return False

def martinGala(apuestaInicial, dinero, numeros):
    #La apuesta es para el color rojo
    dineroJugador = dinero
    apuesta = apuestaInicial
    dineroTiempo = []
    dineroTiempo.append(dineroJugador)
    frecuenciaRelativa = []
    contFrecuencias = 0
    indice = 0
    for i in range(100):
        numero = numeros[i]
        if(dineroJugador >= apuesta):
            if(calcularColor(numero)):
                dineroJugador = dineroJugador + apuesta
                apuesta = apuestaInicial
                contFrecuencias = contFrecuencias + 1
            else:
                dineroJugador = dineroJugador - apuesta
                apuesta = (apuesta * 2)
            dineroTiempo.append(dineroJugador)
            indice += 1
            frecuenciaRelativa.append(contFrecuencias/indice)

    #graficarFrecuencias(frecuenciaRelativa,indice)
    return dineroTiempo, frecuenciaRelativa

def graficarFrecuencias(frecuenciaPromedio):
    plt.bar(range(0,100),frecuenciaPromedio, width=0.6)
    plt.ylabel('Frec. Rel. de la apuesta favorable')
    plt.ylim(0, 1)
    plt.xlabel('Nro iteración')
    plt.show()

def graficoDinero(dineroTiempo, titulo,dineroInicial):
   for i in range(5):
       plt.title(titulo)
       plt.axhline(dineroInicial,color='k', ls="solid")
       plt.plot(dineroTiempo[i], linewidth=0.8)
       plt.xlabel("(Número de tiradas)")
       plt.ylabel("Capital en el tiempo")
       #Me ajustan los x e y
       ax = plt.gca()
       ax.relim()
       ax.autoscale_view()
       #plt.axhline(dineroInicial,color='w', ls="solid",visible=False) #Linea invisible para agregar legend
       #dineroIni = 'Capital inicial: ' + str(dineroInicial)
       #dineroFin = 'Capital Final: ' + str(round(dineroFinal,2))
       #plt.legend((dineroIni,dineroFin), loc="lower left")
       plt.ioff()
   plt.show()

apuestaInicial = 50
capitalJugadorAcotado = 1000
capitalJugadorIdeal = 100_000

dineroMartinGalaAcotado = []
dineroDalembertAcotado = []
dineroDocenaAcotado = []
dineroMartinGalaIdeal = []
dineroDalembertIdeal = []
frecuencias = []


for i in range(5):
    numeros = generarNumeroAleatorios()
    resultadoMartingala = martinGala(apuestaInicial,capitalJugadorIdeal,numeros)
    dineroMartinGalaAcotado.append(resultadoMartingala[0])
    frecuencias.append(resultadoMartingala[1])
frecuencia_Promedio = ((np.asarray(frecuencias[0]) + np.asarray(frecuencias[1]) + np.asarray(frecuencias[2])
                        + np.asarray(frecuencias[3]) + np.asarray(frecuencias[4]))/5)


#graficoDinero(dineroMartinGalaAcotado,'Apuesta MartinGala',capitalJugadorAcotado)
#frecuenciasPromedio = (np.array(frecuencias[0])+np.array(frecuencias[1])+np.array(frecuencias[2])+ np.array(frecuencias[3])+np.array(frecuencias[4])/5)
graficarFrecuencias(frecuencia_Promedio)
