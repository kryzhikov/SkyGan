import os
from PIL import Image

img_dir = r"/home/kirizhik/SkyGan/downloads/pixel sky"
for filename in os.listdir(img_dir):
    try :
        with Image.open(img_dir + "/" + filename) as im:
             print('ok')
        if '.jpg' not in filename:
            os.remove(img_dir + "/" + filename)

    except :
        print(img_dir + "/" + filename)
        os.remove(img_dir + "/" + filename)