import cv2
import mediapipe as mp

# Inicializar MediaPipe para detección de manos
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Cargar la imagen
image = cv2.imread('hand.jpg')

# Convertir BGR a RGB (MediaPipe trabaja con imágenes en RGB)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Inicializar la detección de manos
with mp_hands.Hands(static_image_mode=True, max_num_hands=1) as hands:
    results = hands.process(image_rgb)

    # Si se detectan manos, dibujar los puntos clave en la imagen
    if results.multi_hand_landmarks:
        print(results.multi_hand_landmarks)
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

# Mostrar la imagen con las manos detectadas
cv2.imshow('Manos detectadas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
