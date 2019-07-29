from sky import detect_sky, make_mask
from PIL import Image
import cv2
import numpy as np
def get_mask(path):
    '''
        path to image in jpg format
        returns masked  image as numpy array
    '''
    img = Image.open(path)
    img.save('./tmp/'+path.rstrip('.jpg')+'.png')
    input_image = cv2.imread('./tmp/'+path.rstrip('.jpg')+'.png')
    b1, b2 = detect_sky(input_image)
    if b1 is None:
        print('No sky detected')
        return 
    msl = np.array(make_mask(b1,input_image))
    return msl


def merge_imgs(content, style, mask):
    res = 
    