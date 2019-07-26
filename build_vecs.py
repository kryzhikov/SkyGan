import sys
import os
from img_to_vec import Img2Vec
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from time import time
from saveload import save_obj
input_path = './Styles'


img2vec = Img2Vec(model = 'alexnet')
a = []
names = []
# For each test image, we store the filename and vector as key, value in a dictionary
pics = {}
for file in os.listdir(input_path):
    filename = os.fsdecode(file)
    img = Image.open(os.path.join(input_path, filename))
    vec = img2vec.get_vec(img)
    pics[filename] = vec
    a.append(vec)
    names.append(file)
save_obj(pics,'pics_vocab')
save_obj(a, 'vecs')
save_obj(names, 'names')

