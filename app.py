import os
import tensorflow as tf
import numpy as np
from tensorflow import keras
from skimage import io
from tensorflow.keras.preprocessing import image
from concrete import Hlw
from concrete import ResNetPredictor,DenseNetPredictor
from Context import Context
import io
import random
from flask import Response
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import time 

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()

# You can also use pretrained model from Keras
# Check https://keras.io/applications/

model =tf.keras.models.load_model('resnet.h5',compile=False)
print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img_path, model):
    img = image.load_img(img_path, grayscale=False, target_size=(100, 100))
    show_img = image.load_img(img_path, grayscale=False, target_size=(100, 100))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = np.array(x, 'float32')
    x /= 255
    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        select_pred = request.form.get('predictor')

        print(select_pred)

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        # preds = model_predict(file_path, model)
        # print(preds[0])
        objtst= Hlw()
        ans=objtst.printa()

        ### Testing Strategy Pattern 

        dnetobject = DenseNetPredictor()
        predicament = dnetobject.ml_predict(file_path)
        print("Show predicament : ",predicament)

        ######## Concrete Predictor #########################
        mapping={"resnet": ResNetPredictor(),
        "dnet":DenseNetPredictor(),
        "cnn":,
        "imagenet":}



        ### testing context
        ctuni66=Context(dnetobject)
        preds = ctuni66.nn_predict(file_path)
        print("Show context predictions: ",preds)

        # x = x.reshape([64, 64]);
        global disease_class

        disease_class = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'Potato___Early_blight',
                         'Potato___Late_blight', 'Potato___healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight',
                         'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
                         'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot',
                         'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']
        global a 
        a = 100*preds[0]
        by_class = dict(zip(disease_class,a))
        print(by_class)
        ind=np.argmax(a)
        print('Prediction:', disease_class[ind])
        result=disease_class[ind]
        # def chartTest(disease_class,a):
  
        #     plt.figure(figsize=(8,7))
        #     plt.barh(disease_class,a)   
        #     plt.tight_layout()
        #     plt.savefig('new_plot.png')



        # chartTest(disease_class,a)
        return result
    return None



@app.route('/breedplot')
def breedplot():
    global disease_class
    global a
    img_url='static/images/probability_bars.png'
    plt.figure(figsize=(8,7))
    plt.barh(disease_class,a,color='purple')   
    plt.tight_layout()
    plt.savefig(img_url)
    time.sleep(10)

    return render_template('plotting.html', name = 'probability_bars', url = img_url)








if __name__ == '__main__':
    app.run(port=5002, debug=True)

    # # Serve the app with gevent
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
    # app.run()
