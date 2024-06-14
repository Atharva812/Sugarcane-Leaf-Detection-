# Sugarcane Leaf Disease Detection

This project aims to detect diseases in sugarcane leaves using a web application that allows users to upload or capture images of sugarcane leaves. The application processes the images to predict the type of disease and the confidence level of the prediction.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)


## Features

- **Camera Access**: Capture photos using the device's camera.
- **File Upload**: Upload images from your device.
- **Image Resizing**: Automatically resize images to 256x256 pixels for consistency.
- **Prediction**: Display the predicted disease type and confidence level.



## Requirements

- Python 3.8+
- Flask
- OpenCV
- TensorFlow or PyTorch (depending on the model used)
- HTML5/CSS3
- JavaScript

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/sugarcane-leaf-disease-detection.git
    cd sugarcane-leaf-disease-detection
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the model**:
    - Place your trained model in the `models/` directory. Update the model loading code in `app.py` if necessary.

## Usage

1. **Start the Flask server**:
    ```bash
    python app.py
    ```

2. **Open the application**:
    - Open your web browser and go to `http://127.0.0.1:5000`.

3. **Use the application**:
    - Click on "Access Camera" to use your device's camera.
    - Click on "Capture Photo" to take a picture.
    - Alternatively, click on the upload area to upload an image from your device.
    - The application will display the prediction and confidence level.

## Project Structure

```
sugarcane-leaf-disease-detection/
│
├── app.py                # Flask application
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # HTML file for the web interface
├── static/
│   ├── style.css         # CSS file for styling
│   └── images/           # Folder for static images
├── models/
│   └── model.h5          # Trained model file
└── README.md             # This README file
```




