import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

dataX = np.linspace(0, 9, 100)
#dataY = np.random.uniform(-1, 1, dataX.shape)
dataY = np.cos(dataX*dataX)
dataI = np.arange(len(dataX))

interpX = np.linspace(dataX.min(), dataX.max(), 200)
interpY = [sum([((x - dataX)/(dataX[i] - dataX))[dataI != i].prod() * dataY[i] for i in dataI]) for x in interpX]

sci_Interp3X = np.linspace(dataX.min(), dataX.max(), 200)
sci_3F = interp1d(dataX, dataY, kind='cubic')
sci_Interp3Y = sci_3F(sci_Interp3X)

sci_Interp2X = np.linspace(dataX.min(), dataX.max(), 200)
sci_2F = interp1d(dataX, dataY, kind='cubic')
sci_Interp2Y = sci_2F(sci_Interp2X)

plt.plot(dataX, dataY, 'o')
#plt.plot(interpX, interpY, '-', label="Polinomial")
plt.plot(sci_Interp2X, sci_Interp2Y, '-', label="Scipy quadratic")
plt.plot(sci_Interp3X, sci_Interp3Y, '-', label="Scipy cubic")
plt.plot(interpX, np.sin(interpX*interpX), '-', label="sin(x*x)")
plt.legend()
plt.savefig('Interpolacao.pdf')
plt.close('all')
