import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load pre-trained ResNet50 model (without the final classification layers)
model = ResNet50(weights="imagenet", include_top=False, pooling="avg")

def extract_features(image_path):
    try:
        # Load the image and resize it to the required input size for ResNet50
        image = load_img(image_path, target_size=(224, 224))
        image_array = img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0)
        processed_image = preprocess_input(image_array)

        # Extract features using the pre-trained model
        features = model.predict(processed_image)
        return features.flatten()  # Flatten to make it a 1D array
    except Exception as e:
        print(f"Error in extract_features: {str(e)}")
        return None 