import numpy as np

# Cargar los datos desde un archivo .npy
X = np.load('mi_dataset_X.npy')
Y = np.load('mi_dataset_Y.npy')

# Imprimir los datos cargados
print("Datos cargados:")
print("X:",X)
print("Y:",Y)
