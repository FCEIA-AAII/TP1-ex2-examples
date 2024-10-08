import tensorflow as tf

# Cargar el modelo desde el archivo .h5
model = tf.keras.models.load_model('mi_modelo.h5')

# Mostrar un resumen del modelo para verificar que se ha cargado correctamente
model.summary()

print("Modelo cargado desde 'mi_modelo.h5'.")
