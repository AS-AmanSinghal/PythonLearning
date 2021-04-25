from PIL import Image,ImageFilter

# im = Image.open('./Images/1.png')

# print(im.format)  #it return format of image
# print(im.size)  #return size of image
# print(im.mode)  #return color mode of image

# filteredImage = im.filter(ImageFilter.SHARPEN)  # it is used to set filter in image

# filteredImage = im.convert('L')
# filteredImage.show()
# rotateImage = filteredImage.rotate(180)
# resizeImage = filteredImage.resize((300,300))
# box = (100, 100, 400, 400)
# cropImage = filteredImage.crop(box)
# cropImage.save("cropImage.png","png")


astroNaut = Image.open('./Images/astro.jpg')
# print(astroNaut.size)
# resizeImage = astroNaut.resize((400,400))

# resizeImage.save('thumbnail.jpg')

astroNaut.thumbnail((400,400))
astroNaut.save('thumbnail.jpg')

print(astroNaut.size)