import numpy as np

# Datos de ejemplo (puede ser cualquier array numpy)
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Y = np.array([0, 1, 2])

# Guardar el array en un archivo .npy
np.save('mi_dataset_X.npy', X)
np.save('mi_dataset_Y.npy', Y)

print("Datos guardados!")
