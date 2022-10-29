import numpy as np
import matplotlib.pyplot as plt

L=float(input("Insira o comprimento da parede em metros:"))
n=50
T0=0
T1s=float(input("Insira a temperatura da superfície 1 em Celsius:"))
T2s=float(input("Insira a temperatura da superfície 2 em Celsius:"))
dx=L/n
alpha=float(input("Insira o coeficiente de difusividade térmica do material:"))
t_final=float(input("Insira o instante de tempo final p/ a simulação:"))
dt=0.1

x=np.linspace (dx/2, L-dx/2, n)

T=np.ones(n)*T0
dTdt = np.empty(n)

t=np.arange(0, t_final, dt)

for j in range(1, len(t)):
    plt.clf()
    for i in range(1, n-1):
        dTdt[i] = alpha*(-(T[i]-T[i-1])/dx**2+(T[i+1]-T[i])/dx**2)
    dTdt[0] = alpha*(-(T[0]-T1s)/dx**2+(T[1]-T[0])/dx**2)
    dTdt[n-1] = alpha*(-(T[n-1]-T[n-2])/dx**2+(T2s-T[n-1])/dx**2)
    T = T + dTdt*dt
    plt.figure(1)
    plt.plot(x,T)
    plt.axis([0, L, 0, 50])
    plt.xlabel('Comprimento (m)')
    plt.ylabel('Temperatura (°C)')
    plt.grid(True)
    plt.show()
    plt.pause(0.01)


