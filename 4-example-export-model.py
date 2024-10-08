import tensorflow as tf
from tensorflow.keras import layers, models

# Crear un modelo simple (puedes personalizar este modelo)
model = models.Sequential([
    layers.Input(shape=(10,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(3, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Guardar el modelo en un archivo .h5
model.save('mi_modelo.h5')

print("Modelo guardado en 'mi_modelo.h5'.")
