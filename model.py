#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import numpy as np
from keras.models import load_model
from scipy import misc

##Satart Section
''' Keras took all GPU memory so to limit GPU usage, I have add those lines'''

import tensorflow as tf
from keras.backend.tensorflow_backend import set_session


''' Keras took all GPU memory so to limit GPU usage, I have add those lines'''
## End section


class emotion_model:
    def __init__(self):
        self.config = tf.ConfigProto()
        self.config.gpu_options.per_process_gpu_memory_fraction = 0.1
        set_session(tf.Session(config=self.config))
        self.model = load_model('keras_model/model_5-49-0.62.hdf5')
        self.model.get_config()
        self.target = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
        return

    @classmethod
    def predict_(cls, images):
        config = tf.ConfigProto()
        config.gpu_options.per_process_gpu_memory_fraction = 0.1
        set_session(tf.Session(config=config))
        model = load_model('keras_model/model_5-49-0.62.hdf5')
        model.get_config()
        target = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
        results = []
        for image in images:
            print(image.shape)
            image = image.reshape(1, 1, image.shape[0], image.shape[1])
            print(image.shape)
            model.predict(image)
            results.append(target[np.argmax(model.predict(image))])
        return results

    def predict(self, images):
        results = []
        for image in images:
            print(image.shape)
            image = image.reshape(1, 1, image.shape[0], image.shape[1])
            print(image.shape)
            self.model.predict(image)
            results.append(self.target[np.argmax(self.model.predict(image))])
        return results

    def predict_single_image(self, image):
        return self.predict([image])

    # @classmethod
    # def predict_(cls):
    #     image = misc.imread('image_1.jpeg')/255.
    #
    #     image = 0.2126 * image[:,:,0] + 0.7152 * image[:,:,1] + 0.0722 * image[:,:,2]
    #     image =image.astype('float')
    #     print(type(image))
    #     print(image.shape)
    #     # start_time = time.time()
    #     # duration = "Time to train: %s" % str(time.time() - start_time)
    #     # global detector
    #     detector = emotion_model()
    #     results = detector.predict([image])
    #     print(results)


# model = emotion_model.predict_()
# print(model)
# result = model.predict(images)
# print(result)

