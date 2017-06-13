import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.createLBPHFaceRecognizer();
path='dataSet'

def getImagesWithID(path):
	imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
#	print imagePaths

#getImagesWithID(path)

	faces=[]
	IDs=[]
	for imagePath in imagePaths:
		faceImg=Image.open(imagePath).convert('L');
		faceNp=np.array(faceImg, 'uint8')
		ID=int(os.path.split(imagePath) [-1].split('.')[1])
		faces.append(faceNp)
		IDs.append(ID)
		cv2.imshow("Training", faceNp)
		cv2.waitKey(50)
	return np.array(IDs), faces

IDs, faces= getImagesWithID(path)
recognizer.train(faces,IDs)
recognizer.save('recognizer/trainningData.yml')
print "Error 0"
print"Training done!"
print "Ready to detect."
cv2.destroyAllWindows()