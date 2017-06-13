import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(1);

def insertOrUpdate(Id, Name):
	conn=sqlite3.connect("FaceBase1.db")
	cmd="SELECT * FROM People WHERE ID="+str(Id)
	cursor=conn.execute(cmd)
	isRecordExist=0
	for row in cursor:
		isRecordExist=1
	if isRecordExist==1 :
		cmd="UPDATE People SET Name = '" +srt(Name) + "' WHERE ID="+srt(Id)
	else:
		cmd="INSERT INTO People(ID, Name) Values("+str(Id)+",'"+str(Name)+"')"
	conn.execute(cmd)
	conn.commit()
id= raw_input("Enter User Id : ")
name=raw_input("Enter use name : ")
insertOrUpdate(id, name)

sampleNum=0;


while(True):
	ret, img=cam.read();
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5);

	for(x,y,w,h) in faces:
		sampleNum=sampleNum+1;
		cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg", gray[y:y+h, x:x+w])
		cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0) ,2)
		cv2.waitKey(100);

	cv2.imshow("Face", img);
	cv2.waitKey(1);
	if sampleNum>100:
		print "Sample done !"
		break

cam.release()
cv2.destroyAllWindows() 
