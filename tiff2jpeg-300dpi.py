import sys
import os
import shutil
from PIL import Image
print("\n TIFF to JPG Conversion - 300 DPI \n")
print("\n Developed by A Rajasekaran\n")
print("\n Date: 22 April 2022 \n\n")
for fname in os.listdir():
    if not fname.endswith(".tif"):
        #print(fname)
        continue
    #print(os.path.splitext(fname)[0])
    test = os.path.splitext(fname)[0]
    #print(test)
    image = Image.open(fname)
    name1 = test + ".jpg"
    image.save(name1, 'jpeg', dpi=(300,300), quality=90)
    #print(image.info['dpi'])
print(" JPG Conversion Completed")