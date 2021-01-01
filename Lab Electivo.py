import pandas as pd
import openpyxl
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data1 = pd.read_excel(r"C:\Users\Ignacio\Desktop\Beauchef\6° Semestre\Laboratorio\LAB Electivo\HumedadDia1.xlsx")
data2 = pd.read_excel(r"C:\Users\Ignacio\Desktop\Beauchef\6° Semestre\Laboratorio\LAB Electivo\HumedadDia2.xlsx")
data3 = pd.read_excel(r"C:\Users\Ignacio\Desktop\Beauchef\6° Semestre\Laboratorio\LAB Electivo\HumedadDia3.xlsx")

plt.plot(data1["Fecha"], data1["Humedad"])
xformatter = mdates.DateFormatter('%H:%M')
plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
plt.ylim([0, 1000])
plt.title("Nivel de Humedad Día 1")
plt.ylabel("Lectura Higrómetro [8 bits]")
plt.xlabel("Hora")
plt.show()

plt.plot(data2["Fecha"], data2["Humedad"])
xformatter = mdates.DateFormatter('%H:%M')
plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
plt.ylim([0, 1000])
plt.title("Nivel de Humedad Día 2")
plt.ylabel("Lectura Higrómetro [8 bits]")
plt.xlabel("Hora")
plt.show()

plt.plot(data3["Fecha"], data3["Humedad"])
xformatter = mdates.DateFormatter('%H:%M')
plt.gcf().axes[0].xaxis.set_major_formatter(xformatter)
plt.ylim([0, 1000])
plt.title("Nivel de Humedad Día 3")
plt.ylabel("Lectura Higrómetro [8 bits]")
plt.xlabel("Hora")
plt.show()