'''
Created on Jan 26, 2014

@author: c3h3
'''

import numpy as np
import matplotlib.pyplot as plt

L = 10
n = 2048
t2 = np.linspace(0,L,n+1)
t = t2[:-1]
k = (2*np.pi/L)*np.fft.fftfreq(n,1.0/n)
ks = np.fft.ifftshift(k)

S = (3*np.sin(2*t) + 0.5*np.tanh(0,5*(t-3)) + 0.28*np.exp(-(t-4)**2) \
     + 1.5*np.sin(5*t) + 4*np.cos(3*(t-6)**2))/10 + (t/20)**3

width = 1
slides = np.arange(0,10,0.1)
for i in range(len(slides)):
    f = np.exp(-width*(t-slides[i])**2)
    Sf = np.prod(np.c_[f,S],axis=1)
    Sft = np.fft.fft(Sf)
    
    
    plt.subplot(3,1,1)
    plt.plot(t,S,"k",t,f,"m")
    plt.ylim(-1.25, 1.25)
    
    plt.subplot(3,1,2)
    plt.plot(t,Sf,"k")
    plt.ylim(-1.25, 1.25)
    
    plt.subplot(3,1,3)
    plt.plot(ks,np.abs(np.fft.fftshift(Sft))/max(np.abs(np.fft.fftshift(Sft))),"k")
    plt.xlim(-50, 50)
    
    plt.draw()
    plt.pause(0.2)
    plt.clf()


if __name__ == '__main__':
    pass