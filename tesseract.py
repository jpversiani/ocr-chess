
# %%
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

text = pytesseract.image_to_string(Image.open('data/example1.jpg'))
print(text)

# %%
box_text = pytesseract.image_to_boxes(Image.open('data/example1.jpg'))
print(box_text)

# %%
