##Generador de señales senoidales con Python para el ciclo de publicaicones sobre Procesamiento Digital de Señales
#
#Importanto las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

#Creando un array de mil valores con numpy, de t=0 a t=0.5
t = np.linspace(0,0.5,1000)

#Generando tres funciones seno, con amplitud unitaria
senal_50Hz = np.sin(2*np.pi*50*t)           #frecuencia = 50Hz
senal_200Hz = np.sin(2*np.pi*200*t)         #frecuencia = 200Hz
senal_50Hz_500Hz = senal_50Hz + senal_500Hz #suma de señales

# Gráficando tres subplots.
f, plotArray = plt.subplots(3, sharex=True)
f.suptitle("Señales de ejemplo")
plotArray[0].plot(senal_50Hz, color = 'red')
plotArray[1].plot(senal_200Hz, color = 'green')
plotArray[2].plot(senal_50Hz_200Hz, color = 'blue')
