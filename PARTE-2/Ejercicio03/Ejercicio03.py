from multiprocessing import *
from random import *

def procesoGeneraNotas(cantidad):

    for nota in cantidad:
        nota = round(random.uniform(1.00,10.01))
