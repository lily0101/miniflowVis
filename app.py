# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:38:04 2017

@author: lily0101
"""
import os
import json
from flask import redirect, url_for
from werkzeug import secure_filename
from flask import Flask, request, render_template
from flask import send_from_directory
import numpy as np

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'data')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
all_data = []

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/vis',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        #print("get the file?")
        data = json.loads(request.get_data())
        postName = "strokes";
        if postName in data:
            strokes = data["strokes"]
            print(strokes)
            all_data.append(strokes)
            print(all_data)
            return "success";
        else:
            #save it to file
            filename = os.path.join(app.config['UPLOAD_FOLDER'],data['name']);
            np.save(filename+'.npy',all_data)

        '''
        #code in below is for image of canvas
        file = request.files['image']
        print(file)
        if file and allowed_file(file.filename):
            print("what't wrong with the img")
            filename = secure_filename(file.filename)            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',  
                                    filename=filename))
        '''

    return render_template('index.html')

#for the return file
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/addnumber')
def add():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    return jsonify(result=a + b)

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)



if __name__ == '__main__':
    app.debug = True
    app.run()
