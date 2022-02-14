import numpy as np
import matplotlib.pyplot as plt



name_Data_Water = input("Insert the name file of density of water: ")
name_Data_Air = input("Insert the name file of density of air: ")

data_Water = np.loadtxt(name_Data_Water)
data_Air = np.loadtxt(name_Data_Air)

temperature_Water = data_Water[:, 0]
density_Water = data_Water[:,1]

temperatude_Air = data_Air[:, 0]
density_Air = data_Air[:, 1]

min_x = min(np.concatenate((temperatude_Air, temperature_Water)))
min_y_air = min(density_Air)
min_y_water = min(density_Water)

max_x = max(np.concatenate((temperatude_Air, temperature_Water)))
max_y_air = max(density_Air)
max_y_water = max(density_Water)

plt.plot(temperatude_Air, density_Air, "ro", label="Air density (kg/m$^3$)")
plt.xlabel("Temperature ($\\degree C$)")
plt.ylabel("Air density ($kg/m^3$)", color="red")
plt.legend(loc="upper right")
plt.ylim(min_y_air-1, max_y_air+1)
plt.xlim(min_x-10, max_x+10)

plt.twinx()
plt.plot(temperature_Water, density_Water, "bo", label="Water density (kg/m$^3$)")
plt.ylabel("Water density ($kg/m^3$)", color="blue")
plt.legend(loc="lower right")
plt.ylim(min_y_water-10, max_y_water+10)
plt.show()

plt.close("all")
