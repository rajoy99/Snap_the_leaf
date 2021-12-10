from strategy import Strategy
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

class ResNetPredictor(Strategy):

    model =tf.keras.models.load_model('resnet.h5',compile=False)


    def ml_predict(self,image_path):
        img = image.load_img(image_path, grayscale=False, target_size=(100, 100))
        show_img = image.load_img(image_path, grayscale=False, target_size=(100, 100))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = np.array(x, 'float32')
        x /= 255
        preds = self.model.predict(x)
        return preds


class DenseNetPredictor(Strategy):

    model=tf.keras.models.load_model('densenet.h5',compile=False)

    def ml_predict(self,image_path):
        img = image.load_img(image_path, grayscale=False, target_size=(64,64))
        show_img = image.load_img(image_path, grayscale=False, target_size=(64,64))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = np.array(x, 'float32')
        x /= 255
        preds = self.model.predict(x)
        return preds


class CNNPredictor(Strategy):

    model =tf.keras.models.load_model('baseline_cnn.h5',compile=False)


    def ml_predict(self,image_path):
        img = image.load_img(image_path, grayscale=False, target_size=(64, 64))
        show_img = image.load_img(image_path, grayscale=False, target_size=(64, 64))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = np.array(x, 'float32')
        x /= 255
        preds = self.model.predict(x)
        return preds

class ImageNetPredictor(Strategy):

    model =tf.keras.models.load_model('imagenet.h5',compile=False)


    def ml_predict(self,image_path):
        img = image.load_img(image_path, grayscale=False, target_size=(128, 128))
        show_img = image.load_img(image_path, grayscale=False, target_size=(128, 128))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = np.array(x, 'float32')
        x /= 255
        preds = self.model.predict(x)
        return preds




class Hlw():

    def printa(self):
        return "Hello World"