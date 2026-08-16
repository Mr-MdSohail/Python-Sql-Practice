from PIL import Image
img = Image.open("C:/Users/moham/OneDrive/Desktop/Python/Projects/SPIDERMAN.jpg")
new_img=img.resize((3840,2160))
new_img.save("C:/Users/moham/OneDrive/Desktop/Python/Projects/newimg.jpg")