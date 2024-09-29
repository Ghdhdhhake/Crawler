# Author:wjw
# Development date: 2024/9/29
import pytesseract
from PIL import Image

img = Image.open('download.jpg')
code = pytesseract.image_to_string(img)
print(code)