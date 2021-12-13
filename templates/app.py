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
import checkvalidtion,usefulhasing,filesys,registeruser,connection,detectuser,userrequestforverdict,dataforadminpanel,updateforadminans,findfordetail
import iputuserhelp

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer

# Define a flask app

app = Flask(__name__,template_folder='templates')

app.secret_key='asdsdfsdfs13df_df%&'

# Model saved with Keras model.save()

# You can also use pretrained model from Keras
# Check https://keras.io/applications/

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
    # Face
    return redirect('face')
@app.route('/face', methods=['GET'])
def face():
    return render_template('face.html')
 
 
@app.route('/proceedhome', methods=['POST'])
def proceedhome():
    if not 'userid' in session:
        return redirect('face')


    # Home Page
    return render_template('home.html')
 
 

 
 



@app.route('/predict', methods=['POST'])
def upload():
    if not 'userid' in session:
        return redirect('face')
    if request.method == 'POST':
        
        # Get the file from post request
        f = request.files['file']
        select_pred = request.form.get('predictor')

        print(select_pred)
        path="D:\Snap_the_leaf-master\static"
        adding="\images\probability_bars.png"
        pathforgraph=os.path.join(path,adding)
        email=session['userid']
        pw=session['pw']
        print(email,"   ",pw)
        kala=usefulhasing.u_and_p_hash(email,pw)
        
        folderpath="posts"
        path=os.path.join(path,folderpath)
        folderpath="/".join([folderpath, kala])
        path2=os.path.join(path,kala)
        filename=f.filename
  
        if not filesys.folder_exist(path):
            filesys.create_folder_for_user(path)
            
        
        if not filesys.folder_exist(path2):
                filesys.create_folder_for_user(path2)
        destination = "/".join([path2, filename])
        filepath="/".join([folderpath, filename])
        filepathidentity=usefulhasing.p_hash(filepath) 
            
        userrequestforverdict.requestgiven(filepath,kala,filepathidentity)
        try:
            f.save(destination)

        except:
            print("did not saved")
 
        

        

        objtst= Hlw()
        ans=objtst.printa()

        ### Testing Strategy Pattern 

        dnetobject = DenseNetPredictor()
        predicament = dnetobject.ml_predict(destination)
        print("Show predicament : ",predicament)

        ######## Concrete Predictor #########################
        mapping={"resnet": ResNetPredictor(),
        "dnet":DenseNetPredictor(),
        "cnn":CNNPredictor(),
        "imagenet":ImageNetPredictor()}

        predictor_object = mapping[select_pred]



        ### testing context
        ctuni66=Context(predictor_object)
        preds = ctuni66.nn_predict(destination)
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
        
        
        return render_template("resulting.html",path=filepathidentity,img=img_url)
            
        
        
        
        


    return None

@app.route("/plot/<disease_class>/<a>")
def plot(disease_class, a ):
    
    
   
   
    img_url='static/images/probability_bars.png'
    plt.figure(figsize=(15,6))
    plt.barh(disease_class,a,color='green')   
    plt.tight_layout()
    plt.savefig(img_url)
    return render_template("resulting.html",img_url)


@app.route("/needadminhelp/<identity>")

def needadminhelp(identity):
        if not 'userid' in session:
         return redirect('face')
        email=session['userid']
        pw=session['pw']
        print(email,"   ",pw)
        vdict="r"
        kala=usefulhasing.u_and_p_hash(email,pw)
        print("i am inside needadminhelp")
        iputuserhelp.insertvalues(kala,identity,vdict)
        return redirect(url_for('home'))
        


    


@app.route("/login",methods = ['POST']) 
def login():
     if 'userid' in session:
            print("i am also here")
            return redirect(url_for("home"))
     if request.method == 'POST':
        

        

        
        user = request.form["em"]
        pw=request.form["pw"]
        password =usefulhasing.p_hash(pw)
        print(user)
        print(pw)
        if detectuser.isadmin(user,pw):
            print("i am under adminlogin")
            session['userid']=user
            session['pw']=pw  
            return redirect(url_for("adminpanel"))
        else:

        
        
            if(checkvalidtion.em_exit(user,password)):

                session['userid']=user
                session['pw']=pw
                return redirect(url_for("home"))

            else:
                return redirect(url_for('logout'))
@app.route("/adminpanel")
def adminpanel():
   if not 'userid' in session:
        return redirect('face')
   data= dataforadminpanel.diseaseforconformation()

   return render_template("admin_page.html",data=data)
@app.route("/completeverdict/<x>/<inputVal>")
def completeverdict(x,inputVal):
    if not 'userid' in session:
        return redirect('face')
    
    verdict='c'
    updateforadminans.updatedetails(x,verdict,inputVal)
    return redirect(url_for('adminpanel'))

@app.route("/logout",methods=['GET'])

def logout():
    if request.method=="GET":
     if 'userid' in session:
          session.pop('userid',None)
          session.pop('pw',None)
          

     return redirect(url_for('face'))

@app.route("/home",methods=['GET','POST'])
def home():
    if not 'userid' in session:
        return redirect('face')
    return render_template('home.html')

@app.route("/signup",methods=['GET','POST'])
def signup():

            print("i am for testing")
            session.pop('userid',None)
            session.pop('pw',None)
            if request.method == 'POST':
                print("i am in request method")
                email=request.form["em"]
                pw=request.form['pwd']
                if not detectuser.isadmin(email,pw):
                 print("user is normal")
                  
                 if not checkvalidtion.isregisteredemail(email):
                        
                
                        registeruser.registration(email,pw)
                            
                        kala=usefulhasing.u_and_p_hash(email,pw)  #this will go on folder
                        
                        registeruser.start_with_hash_password(email,pw,kala) #registration done here
                        session['userid']=email
                        session['pw']=pw
                        print("i am here fucker ")
                        return redirect(url_for('home'))
               
            return redirect(url_for('face'))    
@app.route("/farmerdashboard") 
def farmerdashboard():
      if not 'userid' in session:
        return redirect('face')
      email=session['userid']
      pw=session['pw']
      print(email,"   ",pw)
      kala=usefulhasing.u_and_p_hash(email,pw)
        

      a=findfordetail.detailforfarmer(kala)


      return render_template("farmer_dashboard.html",data=a)
@app.route("/tomato_bacterial_spot")
def tomato_bacterial_spot():
    return render_template("tomato_bacterial_spot.html")
    
@app.route("/tomato_early_bright.html")
def tomato_early_bright():
    return render_template("tomato_early_bright")
@app.route("/tomato_late_bright")
def tomato_bacterial_spot():
    return render_template("tomato_bacterial_spot")
@app.route("/tomato_bacterial_spot")
def tomato_bacterial_spot():
    return render_template("tomato_bacterial_spot")
@app.route("/tomato_bacterial_spot")
def tomato_bacterial_spot():
    return render_template("tomato_bacterial_spot")
       





if __name__ == '__main__':
    app.run(host='192.168.0.103',port=5, debug=True)

 