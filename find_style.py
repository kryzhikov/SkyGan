import sys
import os
from img_to_vec import Img2Vec
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from time import time
from saveload import load_obj
input_path = './Styles'

img2vec = Img2Vec(model = 'alexnet')
a = load_obj('vecs')
names = load_obj('names')

a = np.array(a)
start = time()
q = img2vec.get_vec(Image.open('pasha4.jpg'))
score = np.sum(q * a, axis = 1) / np.linalg.norm(a, axis = 1)
topk_idx = np.argsort(score)[::-1]
for i in topk_idx:
    print('> %s\t%s'%(score[i], names[i]))
end = time()
print(end-start)