from PIL import Image
import pytesseract

image = Image.open(
    fp="../datasets/images/example_finance_reporting_slide.png"
)

text = pytesseract.image_to_string(image)

print(text)