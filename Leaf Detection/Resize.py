import os
import tensorflow as tf
from PIL import Image
import uuid

UPLOAD_FOLDER = 'uploads'
original_img_name = '1.png'

original_img_path = os.path.join(os.getcwd(), UPLOAD_FOLDER, original_img_name)

# Function to resize and save images
def resize_and_save(img, output_dir, size):
    try:
        img_resized = img.resize(size, Image.LANCZOS)  # Use Image.LANCZOS for resampling

        # Generate a unique name for the resized image
        resized_img_name = str(uuid.uuid4()) + '_resized.png'
        resized_img_path = os.path.join(output_dir, resized_img_name)

        img_resized.save(resized_img_path)
        return resized_img_name
    except Exception as e:
        print(f"Error processing image: {str(e)}")

# Load the original image
loaded_image = Image.open(original_img_path)

# Convert the loaded image to a NumPy array
original_image_array = tf.keras.preprocessing.image.img_to_array(loaded_image)

# Example usage: Resize the loaded image and save it to the 'API' directory
output_directory = 'C:\\Users\\athar\\OneDrive - MSFT\\Desktop\\API'
target_size = (768, 1024)  # Change this to your desired size

# Create the corresponding output directory structure
output_dir = os.path.join(output_directory, 'example_output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Resize and save the image, and get the name of the resized image
resized_img_name = resize_and_save(loaded_image, output_dir, target_size)
print(f"Resized image saved as: {resized_img_name}")

print('Original Image Array:')
print(original_image_array)
