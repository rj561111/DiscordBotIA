import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

# ================================
# CARGAR MODELO
# ================================
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# ================================
# CARGAR LABELS
# ================================
class_names = open("labels.txt", "r").readlines()

# ================================
# FUNCIÓN DE PREDICCIÓN
# ================================
def predecir_imagen(ruta_imagen):
    image = Image.open(ruta_imagen).convert("RGB")
    image = ImageOps.fit(image, (224, 224))

    image_array = np.asarray(image).astype(np.uint8)
    data = np.expand_dims(image_array, axis=0)

    interpreter.set_tensor(input_details[0]['index'], data)
    interpreter.invoke()

    prediction = interpreter.get_tensor(output_details[0]['index'])

    index = np.argmax(prediction)
    scale, zero_point = output_details[0]['quantization']
    confidence = (prediction[0][index] - zero_point) * scale

    class_name = class_names[index][2:].strip()

    return class_name, confidence