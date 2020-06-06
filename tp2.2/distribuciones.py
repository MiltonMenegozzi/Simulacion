import numpy as np

def distribucion_uniforme(a,b):
    r = np.random.uniform(0,1)
    x = a+(b-a)*r #transformo del intervalo (0,1) al intervalo (a,b)
    return x

def distribucion_exponencial(ex):
    r = np.random.uniform(0,1)
    x = -ex*np.log(r)
    return x

def distribucion_normal(mu,sigma):
    sum = 0.0
    for i in range(12):
        r = np.random.uniform(0,1)
        sum = sum + r
    x = sigma * (sum - 6.0) + mu
    return x

def distribucion_gamma(k,alpha):
    tr = 1.0
    for i in range(k):
        r = np.random.uniform(0,1)
        tr = tr *  r
    x = -np.log(tr)/alpha
    return x

def distribucion_pascal(k,q):
    tr = 1.0
    qr = np.log(q)
    for i in range(k):
        r = np.random.uniform(0,1)
        tr = tr * r
    nx = np.log(tr)/qr
    x = nx
    return x

def distribucion_binomial(n,p):
    x = 0.0
    for i in range(n):
        r = np.random.uniform(0,1)
        if (r-p) < 0:
            x += 1
    return x

def distribucion_hipergeometrica(tn,ns,p):
    #TN = N
    #NS = n
    x = 0.0
    for i in range(ns):
        r = np.random.uniform(0,1)
        if (r-p) > 0:
            s = 0.0
        else:
            s = 1.0
            x = x + 1.0
        p = (tn*p-s) / (tn-1.0)
        tn = tn - 1.0
    return x

def distribucion_poisson(p):
    #p = lambda
    x = 0.0
    b = np.exp(-p)
    tr = 1.0
    while (tr-b) >= 0:
        r = np.random.uniform(0,1)
        tr = tr * r
        if(tr-b >= 0):
            x = x + 1.0
    return x



