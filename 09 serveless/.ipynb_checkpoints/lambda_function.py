# lambda_function.py

import tensorflow as tf
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# Load the TFLite model (adjust the path as needed)
interpreter = tf.lite.Interpreter(model_path="path/to/your_model.tflite")
interpreter.allocate_tensors()

def lambda_handler(event, context):
    # Example of processing an image from a URL
    image_url = event.get("url")
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Preprocess the image (resize, normalize, etc.)
    image = image.resize((200, 200))  # Adjust the size for your model input
    preprocessed_img = np.expand_dims(np.array(image) / 255.0, axis=0).astype(np.float32)

    # Get input and output tensor details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Set the tensor value
    interpreter.set_tensor(input_details[0]['index'], preprocessed_img)
    interpreter.invoke()

    # Get the result
    output = interpreter.get_tensor(output_details[0]['index'])
    
    # Return the result
    return output.tolist()  # Returning the output as a list (you can modify this depending on your needs)
