
# This is a comment

# %%
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
path = 'data/example1.png'
img = Image.open(path)
pix = img.load()

text = pytesseract.image_to_string(Image.open('data/temp.jpg'))
print(text)

# %%
