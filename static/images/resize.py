from PIL import Image
import glob

size = 512,512

files = glob.glob("./*.jpg")
for file in files:
    im = Image.open(file)
    print(file,im.size)
    im.thumbnail((1500, 1000))
    im.save(file + '_thumbnail'+".jpg")