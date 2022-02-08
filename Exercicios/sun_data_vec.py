import numpy as np

# Dados horas de sol por mes
Oxford_sun_hours = np.loadtxt("Oxford_sun_hours.dat", delimiter=",")
monthly_mean = (np.array(Oxford_sun_hours).mean(axis=0)) # Media de horas por mes
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
               'Oct', 'Nov', 'Dec']
# Imprimindo as horas media de sol por mes
for value, name in zip(monthly_mean, month_names):
    print(f"{name}:\t{value:.1f}")

# Dados do mes com maior media de horas de sol
max_value = max(monthly_mean)
month_max = month_names[monthly_mean.argmax()]

print(f"{month_max} has best weather with {max_value:.1f} sun hours"
      + " on average")

# Dados da media de horas por decada
decade_mean = ((np.array((np.array_split((((Oxford_sun_hours[1:, 0] + 
                                            Oxford_sun_hours[:-1, 11]))), 8))))
               .sum(axis=1))/600

# Imprimindo valores da media de horas por decada
for i, value in enumerate(decade_mean):
    print(f"Decade {1930+i*10}-{1939+i*10}: {value:.1f}")
