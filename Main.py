# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 21:09:51 2018

@author: rpark
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sp

samplingfrequency=44000
frequency =220

noprimes = list(set(j for i in range(2, 20) for j in range(i*2, 400, i)))

primes = [x for x in range(1, 400) if x not in noprimes]

length =3
time = np.linspace(0,length,samplingfrequency*length+1)

n=0
sound=np.zeros(len(time))
for prime in primes:
    harmonic=[]
    n+=1
    sound+=np.sin(time*n*frequency*2*np.pi)/prime*0.6

noise = np.random.normal(0, 0.03, size=len(time))

envolope=1/(1+np.exp((0.5-time)*30)+np.exp((time-2.5)*30))
sound=(sound+noise)*envolope
sp.write('test.wav',samplingfrequency,sound)
plt.plot(sound)

    
