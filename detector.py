import cv2
import numpy as np
from PIL import Image
import pickle
import sqlite3


faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(1);

rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer/trainningData.yml")
 
def getProfile(id):
	conn=sqlite3.connect("FaceBase1.db")
	cmd="SELECT * FROM People WHERE ID ="+str(id)
	cursor=conn.execute(cmd)
	profile=None
	for row in cursor:
		profile=row
	conn.close()
	return profile 


#id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX,1,.5,0,2,1)
fontColor= (194,244,66)
while(True):
	ret, img=cam.read();
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5);

	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y),(x+w,y+h),(244,229,66) ,2)
		id, conf=rec.predict(gray[y:y+h, x:x+w])
		
		profile=getProfile(id)
		if (profile!=None):   
			cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[1]),(x,y+h+30),font,fontColor);
			cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[2]),(x,y+h+60),font,fontColor);
			cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[3]),(x,y+h+90),font,fontColor);
			cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[4]),(x,y+h+120),font,fontColor);
	cv2.imshow("Face", img);
	if (cv2.waitKey(1) == ord('q')):
		break;


		cam.release()
		cv2.destroyAllwindows() 
