import os
from PIL import Image

existFolder = 'New\\'
newFolder = 'AMAN\\'

if not os.path.isdir(newFolder):
    os.mkdir(f'./{newFolder}')

for filename in os.listdir(f'./{existFolder}'):
    image = Image.open(f'./{existFolder}{filename}')
    imageName = os.path.splitext(filename)[0]
    print(f'{newFolder}{imageName}.jpg')
    image.convert('RGB').save(f'{newFolder}{imageName}.jpg')
    print(image)


