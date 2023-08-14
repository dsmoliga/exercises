from PIL import Image

image = Image.open("E:\Projects\Learning Python\pillow\photo.jpg")

width, height = image.size

print(f"Szerokość obrazka: {width}px")
print(f"Wysokość obrazka: {height}px")