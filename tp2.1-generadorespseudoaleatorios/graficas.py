import matplotlib.pyplot as plt

def graficoCircular(par, impar, titulo):
   plt.title(str(titulo))
   par = par
   impar = impar
   variables = [par, impar]
   nombres = ["Pares", "Impares"]
   plt.pie(variables, labels=nombres, autopct='%1.1f%%', shadow=True)
   plt.axis("equal")
   plt.legend(loc='lower right')
   plt.show()
