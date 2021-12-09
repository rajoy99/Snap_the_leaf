from strategy import Strategy

# class ResNetPredictor(Strategy):

#     model =tf.keras.models.load_model('resnet.h5',compile=False)


#     def ml_predict(self,image_path):
#         img = image.load_img(img_path, grayscale=False, target_size=(100, 100))
#         show_img = image.load_img(img_path, grayscale=False, target_size=(100, 100))
#         x = image.img_to_array(img)
#         x = np.expand_dims(x, axis=0)
#         x = np.array(x, 'float32')
#         x /= 255
#         preds = model.predict(x)
#         return preds

class Hlw():

    def printa(self):
        return "Hello World"