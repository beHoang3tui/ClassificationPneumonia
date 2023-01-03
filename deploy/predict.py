import numpy as np 
import pandas as pd 
from numpy import *
import tensorflow as tf
from PIL import Image 

model = tf.keras.models.load_model('model/model2.10.h5')

def Predict (image):
    pred = model.predict(image.reshape(1, 224 , 224, 3))
    return {'Có bị bệnh viên phổi' if np.argmax(pred) == 1 else 'Không bị bệnh viêm phổi '}