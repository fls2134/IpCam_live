from flask import Flask
import urllib.request
import numpy as np
import cv2
from flask_cors import CORS
import base64
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return 'main'

@app.route('/img')
def send_img():
    req = urllib.request.urlopen('http://192.168.00.00/jpg/')
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    
    jpg_img = cv2.imencode('.jpg', img)
    img_bytes = base64.b64encode(jpg_img[1]).decode('utf-8')
    
    # delay
    time.sleep(0.3) 
    return img_bytes, 200, {'Content-Type': "image/jpeg;"}