import pytesseract
from PIL import Image

def parse_image(path):

    img = Image.open(path)

    text = pytesseract.image_to_string(img)

    return text