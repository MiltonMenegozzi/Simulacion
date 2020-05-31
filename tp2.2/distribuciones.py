import numpy as np

def distribucion_uniforme(a,b):
    for i in range(100):
        r = np.random.rand()
        x = a+(b-a)*r #Lo transforma a mi intervalo a,b
        #return x
        print(x)

def distribucion_exponencial(ex):
    for i in range(100):
        r = np.random.rand()
        x = ex-np.log(r)
        print(x)
