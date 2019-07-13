#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import numpy as np
from keras.models import load_model

##Satart Section
''' Keras took all GPU memory so to limit GPU usage, I have add those lines'''

import tensorflow as tf
from keras.backend.tensorflow_backend import set_session

config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.1
set_session(tf.Session(config=config))
''' Keras took all GPU memory so to limit GPU usage, I have add those lines'''
## End section


class emotion_model:
    def __init__(self):
        self.model = load_model('keras_model/model_5-49-0.62.hdf5')
        self.model.get_config()
        self.target = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
        return

    def predict(self, images):
        results = []
        for image in images:
            print(image.shape)
            image = image.reshape(1, 1, image.shape[0], image.shape[1])
            results.append(self.target[np.argmax(self.model.predict(image))])
        return results

    def predict_single_image(self, image):
        return self.predict([image])


# model = emotion_model()
# result = model.predict(images)
# print(result)

