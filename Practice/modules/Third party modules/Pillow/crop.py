from PIL import Image
img = Image.open("C:/Users/moham/OneDrive/Desktop/Python/Projects/SPIDERMAN.jpg")
cropped = img.crop((10,20,300,40))
cropped.show()