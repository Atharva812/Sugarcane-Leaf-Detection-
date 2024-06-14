from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import tensorflow as tf
from PIL import Image
import io
import os
import uuid
import base64

app = Flask(__name__, static_folder='static')

model_path = "Version_1"
model = load_model(model_path)

CLASS_NAMES = ['Banded Chlorosis', 'Brown Rust', 'Brown Spot', 'Dried Leaves', 'Grassy Shoot', 'Healthy Leaves', 'Pokkah Boeng', 'Sett Rot', 'Smut', 'Viral Disease', 'Yellow Leaf']

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def preprocess_image(image_data):
    image_bytes = base64.b64decode(image_data.split(',')[1])
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((256, 256))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    return image_array

# Ensure the 'uploads' folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def resize_and_save(img, output_dir, size):
    try:
        img_resized = img.resize(size, Image.LANCZOS)  # Use Image.LANCZOS for resampling
        resized_img_name = str(uuid.uuid4()) + '_resized.png'
        resized_img_path = os.path.join(output_dir, resized_img_name)
        img_resized.save(resized_img_path)
        return resized_img_name
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return None

@app.route('/')
def index():
    return render_template("SugarcaneLeafdetection.html")

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        data = request.get_json()
        image_data = data.get('image', '')

        preprocessed_image = preprocess_image(image_data)

        # Example usage: Resize the loaded image and save it to the 'API' directory
        output_directory = 'C:\\Users\\athar\\OneDrive - MSFT\\Desktop\\API'
        target_size = (256, 256)  # Change this to your desired size

        # Create the corresponding output directory structure
        output_dir = os.path.join(output_directory, 'example_output')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Resize and save the image, and get the name of the resized image
        resized_img_name = resize_and_save(Image.fromarray(preprocessed_image.astype('uint8')), output_dir, target_size)

        if resized_img_name is not None:
            print(f"Resized image saved as: {resized_img_name}")

            # Further processing with the model if needed
            predictions = model.predict(preprocessed_image.reshape(1, *preprocessed_image.shape))
            predicted_class_index = tf.argmax(predictions[0])
            predicted_class = CLASS_NAMES[predicted_class_index]
            confidence = float(tf.reduce_max(predictions))

            return jsonify({'predicted_class': predicted_class, 'confidence': confidence, 'resized_img_name': resized_img_name})

        else:
            return jsonify({'error': 'Error processing image'}), 500

    except Exception as e:
        print(f'Error processing image: {e}')
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
