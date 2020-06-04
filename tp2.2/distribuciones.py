import numpy as np

def distribucion_uniforme(a,b):
    r = np.random.uniform(0,1)
    x = a+(b-a)*r #transformo del intervalo (0,1) al intervalo (a,b)
    return x

def distribucion_exponencial(ex):
    r = np.random.uniform(0,1)
    x = -ex*np.log(r)
    return x
