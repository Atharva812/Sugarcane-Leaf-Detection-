from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import tensorflow as tf
import base64
from PIL import Image
import io

app = Flask(__name__, static_folder='static')

model_path = "Version_1"
model = load_model(model_path)

CLASS_NAMES = ['Banded Chlorosis', 'Brown Rust', 'Brown Spot', 'Dried Leaves', 'Grassy Shoot', 'Healthy Leaves', 'Pokkah Boeng', 'Sett Rot', 'Smut', 'Viral Disease', 'Yellow Leaf']

def preprocess_image(image_data):
    image_bytes = base64.b64decode(image_data.split(',')[1])
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((256, 256))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    return image_array

@app.route('/')
def index():
   return render_template("SugarcaneLeafdetection.html")

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        data = request.get_json()
        image_data = data.get('image', '')
      
        preprocessed_image = preprocess_image(image_data)
       
        predictions = model.predict(preprocessed_image.reshape(1, *preprocessed_image.shape))
        predicted_class_index = tf.argmax(predictions[0])
        predicted_class = CLASS_NAMES[predicted_class_index]
        confidence = float(tf.reduce_max(predictions))
   
        return jsonify({'predicted_class': predicted_class, 'confidence': confidence})

    except Exception as e:
        print(f'Error processing image: {e}')
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)