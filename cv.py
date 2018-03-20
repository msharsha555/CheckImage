import os
from flask import Flask, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
import matplotlib.pyplot as plt
import cv2
from skimage import measure
import numpy as np

UPLOAD_FOLDER = '/home/harsha/CheckImage/Images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
    	if 'file' in request.files:
        	file = request.files['file']
        	if file and allowed_file(file.filename):
        		filename = secure_filename(file.filename)
        		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        		destination = "/".join([UPLOAD_FOLDER, filename])
        		print(filename)
        		print(destination)
        		string ="The uploaded image  " + str(filename) + " is "
        		image = cv2.imread(destination)
        		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        		var = cv2.Laplacian(gray, cv2.CV_64F).var()
        		print(var)
        		global blur
        		if var < 90:
        			blur =1
        		else:
        			blur=0
        		
        		blur_image = cv2.GaussianBlur(gray, (5, 5), 0)
        		thresh_image = cv2.threshold (blur_image, 225, 255, cv2.THRESH_BINARY)[1]
        		label_image = measure.label(thresh_image, 8, 0)
        		global flash
        		for label in np.unique(label_image):
        			if label:
        				Mask = np.zeros(thresh_image.shape, dtype="uint8") 
        				Mask[label_image == label] = 255
        				numPixels = cv2.countNonZero(Mask)

        				if numPixels > 400:
        					flash=1
        					break 
        				else:
        					flash=0

        		histr = cv2.calcHist([image],[0],None,[256],[0,256])
        		max_hist=max(histr)
        		scale = len(histr)
        		global exposed
        		for i in range(0,scale):
        			if histr[i] == max_hist:
        				index = i
        		
        		if index < 30:
        			exposed = -1
        		elif index > 225:
        			exposed = 1
        		else:
        			exposed=0

        		if blur == 1:
        			string+="[Blurred] and "
        		else:
        			string+="[NOT Blurred] and "
        		
        		if exposed == -1:
        			string+="[UnderExposed] and "	
        		elif exposed==1:
        			string+="[OverExposed] and "
        		else:
        			string+="taken in [Good Lightning] conditions and	"
        		
        		if flash:
        			string+=" contains [Flash/Glare]"
        		else:
        			string+=" does NOT contain [Flash/Glare]"

        		return string
    
    return 	render_template('upload.html')

if __name__ == "__main__":
	app.run()
