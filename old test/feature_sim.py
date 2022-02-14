import numpy as np
import keras
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
import cv2

#load pretrain model
vgg16 = keras.applications.VGG16(weights='imagenet', include_top=False, pooling='max', input_shape=(512, 512, 3))


def get_feature_vector(img):
    img = cv2.resize(img, (1000, 1000))
    img = img[0:512,0:512]
    #轉灰階
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #色彩偏移
    img= np.float32(img)
    avg_grey = np.sum(img)/(512*512)
    L_change = 100/avg_grey
    img= img*L_change

    cond= img[:,:] > 255
    img[cond] = 255

    img=img.astype('uint8')
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    #VGG獲取特徵
    feature_vector = vgg16.predict(img.reshape(1, 512, 512, 3))
    return feature_vector 

 
def calculate_similarity(vector1, vector2):
    return cosine_similarity(vector1, vector2)[0][0] #return float 


