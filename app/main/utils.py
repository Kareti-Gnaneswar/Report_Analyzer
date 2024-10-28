import pytesseract
from PIL import Image
import joblib
import os

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Update with your Tesseract path

# Load your pre-trained model for disease prediction
model_path = os.path.join('models', 'disease_prediction_model.pkl')
disease_model = joblib.load(model_path)

def extract_text_from_image(image_path):
    """Extracts text from an uploaded image file."""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def predict_disease_from_text(text):
    """Predicts disease from extracted text."""
    # Process text data as per your model's requirements
    # This could involve text vectorization or keyword-based filtering
    processed_text = text  # Placeholder for actual preprocessing

    # Predict using the pre-trained model
    prediction = disease_model.predict([processed_text])
    return prediction[0] if prediction else "No prediction available"
