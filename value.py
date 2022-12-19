import numpy as np
import matplotlib.pyplot as plt

from keras.layers import Dense, Conv2D, MaxPool2D , Dropout, Flatten
from keras.models import Sequential
from keras.preprocessing import image

train_datagen = image.ImageDataGenerator(rescale = 1/255,horizontal_flip = True , zoom_range = 0.2, shear_range= 0.2)

