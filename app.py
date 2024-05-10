from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            destination = float(request.form['destination'])
            passanger = float(request.form['passanger'])
            weather = float(request.form['weather'])
            temparature = float(request.form['temparature'])
            time = float(request.form['time'])
            coupon = float(request.form['coupon'])
            expiration = float(request.form['expiration'])
            gender = float(request.form['gender'])
            age = float(request.form['age'])
            maritalStatus = float(request.form['maritalStatus'])
            has_children = int(request.form['has_children'])
            education = float(request.form['education'])
            income = float(request.form['income'])
            to_coupon = int(request.form['to_coupon'])
            coupon_freq = float(request.form['coupon_freq'])
            occupation_class = int(request.form['occupation_class'])
       
         
            data = [destination, passanger, weather, temparature, time, coupon, expiration, gender, age, maritalStatus, has_children, education, income, Y, to_coupon, coupon_freq, occupation_class]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)