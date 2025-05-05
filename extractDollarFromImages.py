import easyocr
import re

reader = easyocr.Reader(['en'])


def dollar_str_to_int(dollar_str):
    if not dollar_str.startswith('$'):
        return None  # Not a valid dollar string
    try:
        value = float(dollar_str[1:])  # Remove $ and convert to float
        return int(value)  # Drop cents
    except ValueError:
        return None  # Handle cases like "$abc"

def extract_dollar_amount_from_text(text):
    text = text.replace('S', '$')  # Fix OCR mistakes
    match = re.search(r"\$\d+(?:\.\d{1,2})?", text)
    if match:
        return match.group()
    return None

def start(image_path):
    results = reader.readtext(image_path)

    found = None
    for (_, text, _) in results:
        amount = extract_dollar_amount_from_text(text)
        if amount:
            found = amount
            break
    if found:
        return dollar_str_to_int(found)
    return None
