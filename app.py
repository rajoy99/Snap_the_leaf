import os
import tensorflow as tf
import numpy as np
from tensorflow import keras
from skimage import io
from tensorflow.keras.preprocessing import image
from concrete import Hlw
from concrete import ResNetPredictor,DenseNetPredictor,CNNPredictor,ImageNetPredictor
from Context import Context
import io
import random
from flask import Response,session
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import time 
import checkvalidtion,usefulhasing,filesys,registeruser,connection


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
    
    # first page
    return render_template("face.html")


@app.route('/predict', methods=['POST'])
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
        "cnn":CNNPredictor(),
        "imagenet":ImageNetPredictor()}

        predictor_object = mapping[select_pred]



        ### testing context
        ctuni66=Context(predictor_object)
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
        img_url='static/images/probability_bars.png'
        plt.figure(figsize=(15,6))
        plt.barh(disease_class,a,color='green')   
        plt.tight_layout()
        plt.savefig(img_url)
        
        
        return render_template('resulting.html',result=result,img_url=img_url)


    return None


@app.route("/login",methods = ['POST']) 
def login():
    
    if request.method == 'POST':
        print("i am here")

        if 'userid' in session:
            print("i am also here")
            return render_template("newsfeed.html")
        if request.method=="POST":
            user = request.form["em"]
            pw=request.form["pw"]
            print(user)
            print(pw)
            
            password =usefulhasing.p_hash(pw)
            if(checkvalidtion.em_exit(user,password)):

                session['userid']=user
                session['pw']=pw
                return redirect("/newsfeed")

            else:
                return redirect('logout')



@app.route("/signup",methods=['GET','POST'])
def signup():
            session.pop('userid',None)
            session.pop('pw',None)
            if request.method == 'POST':
                email=request.form["email"]
                pw=request.form['pswd']
                firstname=request.form['firstname']
                country=request.form['country']
                if not checkvalidtion.isregisteredemail(email):
                        
                
                        registeruser.registration(email,pw)
                            
                        kala=usefulhasing.u_and_p_hash(email,pw) #this will go on folder
                        path="F:\websesh\static"
                        folder="userprofile"
                        folderpath="userprofile"
                        path=os.path.join(path,folder)
                        path2=os.path.join(path,kala)
                        folderpath="/".join([folderpath, kala])#this will go on path
                        
                        
                        print(kala)
                        
                        if not filesys.folder_exist(path):
                            filesys.create_folder_for_user(path)
                            
                            
                        if not filesys.folder_exist(path2):
                                filesys.create_folder_for_user(path2)
                       
                        for upload in request.files.getlist("file"):
                            print("mey tera",upload.filename)
                            filename = upload.filename    #this will go on file name 
                            print("sudir vai sudi ",filename)
                               
                            ext = os.path.splitext(filename)[1]
                            if (ext == ".jpg") or (ext == ".png"):
                                        print("File supported moving on...")
                            
                            
                            destination = "/".join([path2, filename])
                            filepath="/".join([folderpath, filename])#this is the ultimate folder path
                            
                            print("Accept incoming file:", filename)
                            print("Save it to:", destination)
                            
                            registeruser.start_with_hash_password(email,pw,firstname,country,kala,filepath)#registration done here
                            
                            
                            

                            session['userid']=email
                            session['pw']=pw
                            upload.save(destination)
                session['userid']=email
                session['pw']=pw
       
                return  redirect("newsfeed")





if __name__ == '__main__':
    app.run(host='192.168.0.103',port=5, debug=True)

 