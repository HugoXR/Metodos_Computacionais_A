import numpy as np
import matplotlib.pyplot as plt

G = 9.81 # acceleration of gravity in m/s^2
S = 7.9e-2 # air-water surface tension in N/m
P = 1000 # density of water in kg/m^3
H = 50 # water depth in m

lambda_wave_small = np.linspace(0.001, 0.1) # length wave in m
lambda_wave_larger = np.linspace(1, 2000) # lenght wave in m

def c_vel(lambda_wave):
    """Return the wave velocity of a fluid"""
    return np.sqrt((G*lambda_wave/2*np.pi)*(1+S*(4*np.pi**2/(P*G*(lambda_wave**2))))*(np.tanh(2*np.pi*H/lambda_wave))) # velocity of wave function

c_small = c_vel(lambda_wave_small)
c_larger = c_vel(lambda_wave_larger)

plt.plot(lambda_wave_small, c_small, "-b")
plt.xlabel("$\\lambda (m)$")
plt.ylabel("Velocity $(m/s)$")
plt.show()
plt.close('all')


plt.plot(lambda_wave_larger, c_larger, "-r")
plt.xlabel("$\\lambda (m)$")
plt.ylabel("Velocity $(m/s)$")
plt.show()
plt.close('all')



