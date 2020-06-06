import matplotlib.pyplot as plt

def histograma(distribucion):
    plt.hist(distribucion,density=True,histtype='stepfilled', bins=50)
    plt.show()
