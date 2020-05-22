import numpy as np
import matplotlib.pyplot as plt

def generarNumeroAleatorios():
   listaAleatorios = []
   for i in range(1000):
       listaAleatorios.append(np.random.randint(0,37))
   return listaAleatorios

def calcularColor(numero):
  #ROJO DEVUELVE TRUE
  if numero in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
      return True
  return False

def calcularParidad(numero):
  if numero % 2 == 0:
      return True
  return False

def calcularColumna(numero, jugada):
    if(jugada == 1):
        if(numero<12):
            return True
        return False

    if(jugada == 2):
        if(13<numero<24):
            return True
        return False

    if(jugada == 3):
        if(24<numero<36):
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
    for i in range(1000):
        numero = numeros[i]
        if(dineroJugador >= apuesta):
            if(calcularColor(numero)):
                dineroJugador = dineroJugador + (apuesta*2-apuesta)
                apuesta = apuestaInicial
                contFrecuencias = contFrecuencias + 1
            else:
                dineroJugador = dineroJugador - apuesta
                apuesta = (apuesta * 2)
            dineroTiempo.append(dineroJugador)
            indice += 1
            frecuenciaRelativa.append(contFrecuencias/indice)

    graficarFrecuencias(frecuenciaRelativa,indice)
    return dineroTiempo

def graficoDinero(dineroTiempo):
   #plt.title(titulo+'\nDinero final jugador: '+dineroJugador)
   plt.plot(dineroTiempo)
   plt.xlabel("(Número de tiradas)")
   plt.ylabel("Capital en el tiempo")
   #Me ajustan los x e y
   ax = plt.gca()
   ax.relim()
   ax.autoscale_view()
   plt.show()

def graficarFrecuencias(frecuenciaRelativa,indice):
    plt.bar(range(0,indice),frecuenciaRelativa)
    plt.ylabel('Frec. Rel. de la apuesta favorable')
    plt.ylim(0, 1)
    plt.xlabel('Nro iteración')
    plt.show()

def dalembert(apuesta, dinero, numeros):
    #La apuesta es para color rojo
    dineroJugador = dinero
    apuesta = apuesta
    indice = 0
    contFrecuencias = 0
    frecuenciaRelativa = []
    dineroTiempo = []
    dineroTiempo.append(dinero)
    for i in range(1000):
            numero = numeros[i]
            if(dineroJugador >= apuesta):
                if calcularColor(numero):
                    dineroJugador = dineroJugador + (apuesta*2 - apuesta)
                    contFrecuencias += 1
                    if apuesta>1:
                        apuesta = apuesta - 1
                else:
                    dineroJugador = dineroJugador - apuesta
                    apuesta = apuesta + 1
                dineroTiempo.append(dineroJugador)
                indice += 1
                frecuenciaRelativa.append(contFrecuencias/indice)

    graficarFrecuencias(frecuenciaRelativa,indice)
    return dineroTiempo

def apostarDocena(capital, jugada, listaAleatorio):
  apuesta = 50
  dineroJugador = capital
  dineroTiempo = []
  contGanadas = 0
  contPerdidas = 0
  dineroTiempo.append(dineroJugador)
  for i in range(1000):
      if(dineroJugador >= apuesta):
          numero = listaAleatorio[i]
          if(calcularColumna(numero, jugada)):
              dineroJugador = dineroJugador + (apuesta * 1/3)
              contGanadas += 1
          else:
              dineroJugador = dineroJugador - apuesta
              contPerdidas += 1
          dineroTiempo.append(dineroJugador)
          totalIteraciones = i
  periodoBeneficios = contGanadas/totalIteraciones
  if (jugada == 1):
      titulo = 'Apuesta a: '+ str(jugada)+'ªera Docena'
  if (jugada == 2):
      titulo = 'Apuesta a: '+ str(jugada)+'ªda Docena'
  if (jugada == 3):
      titulo = 'Apuesta a: '+ str(jugada)+'ªra Docena'
  #graficoDinero(dineroTiempo,titulo,capital,periodoBeneficios,str(round(dineroJugador,4)))
  return dineroTiempo

numeros = generarNumeroAleatorios()
apuestaInicial = 50
capitalJugadorAcotado = 1000
capitalJugadorIdeal = 100_000
graficoDinero(martinGala(apuestaInicial,capitalJugadorIdeal,numeros))
graficoDinero(dalembert(apuestaInicial,capitalJugadorIdeal,numeros))
graficoDinero(martinGala(apuestaInicial,capitalJugadorAcotado,numeros))
graficoDinero(dalembert(1,capitalJugadorAcotado,numeros))
