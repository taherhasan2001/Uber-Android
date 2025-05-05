from PIL import Image
import pytesseract
import cv2
import numpy as np
import re

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def preprocess_currency_image(image_path):
    """Specialized preprocessing for currency extraction"""
    try:
        # Read and convert to grayscale
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # High-contrast binarization
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

        # Noise removal
        kernel = np.ones((2, 2), np.uint8)
        processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # Scale up small text (2x)
        if img.shape[0] < 100 or img.shape[1] < 100:
            processed = cv2.resize(processed, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

        return cv2.bitwise_not(processed)  # Return to black-on-white

    except Exception as e:
        print(f"Preprocessing error: {e}")
        return Image.open(image_path)


def extract_currency(image_path):
    """Extracts currency values ($X.XX format) from image"""
    try:
        # Specialized preprocessing
        processed_img = preprocess_currency_image(image_path)

        # Convert to PIL format if needed
        if isinstance(processed_img, np.ndarray):
            processed_img = Image.fromarray(processed_img)

        # Currency-specific OCR config
        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=$0123456789.'
        raw_text = pytesseract.image_to_string(processed_img, config=custom_config)

        # Find all currency patterns
        currency_values = re.findall(r'\$\d+\.\d{2}', raw_text)

        if currency_values:
            return currency_values[0]  # Return first match
        return "No currency detected"

    except Exception as e:
        return f"Error: {str(e)}"

