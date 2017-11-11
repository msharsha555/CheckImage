# CheckImage
A simple web interface where you can upload an image to the local server and get instantaneous results about the image.

Instructions:

First of all install flask web framework on your system using Anaconda


**COMMAND : conda install flask**

Install other libraries like numpy,cv2,malplotlib,skimage which are also necessary to process the image.

Run the .py file using the following command

**COMMAND :python3 cv.py**

Voila! Your server is running on port 5000

Go to google chrome and type **localhost:5000**

You can see a simple webpage asking to upload an image.

Upload the image and you can see instantaneous results about the image 

The following details are included in the result:


1.To check whether the image is **blurred** or **NOT blurred**


2.To check whether the image is **overexposed** or **underexposed** or taken under **good lightning** conditions


3.To check whether the image contains **flash or glare**

**Demo** for an example image 

Initial Page you see when you type localhost:5000 in the browser:

![alt text](https://user-images.githubusercontent.com/17835484/32687034-b47ea5d0-c6d8-11e7-8e8a-abc646922d26.jpg)

The uploaded image is the following:

<img src="https://user-images.githubusercontent.com/17835484/32687057-783137fe-c6d9-11e7-99ac-373ee80ee1f1.jpg" width="994" height="600">

After processing the image:

![alt text](https://user-images.githubusercontent.com/17835484/32687036-b6d826d0-c6d8-11e7-9b9e-8607e690c497.jpg)

Terminal after successful image processing ( 200 implies successful completion ):

![alt text](https://user-images.githubusercontent.com/17835484/32687239-2b4bea10-c6de-11e7-8432-4d0d789dfb51.png)


