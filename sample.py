from pydarknet import Detector, Image
import cv2
import os
import time

net = Detector(bytes("config-files/face.cfg", encoding="utf-8"), bytes("face.weights", encoding="utf-8"), 0, bytes("config-files/face.data",encoding="utf-8"))
start_time = time.time()

currentPath = os.getcwd()
savingDirectory = currentPath + "/results"
if not os.path.exists(savingDirectory):
	os.makedirs(savingDirectory)

#give the photo directory
imageDir = "samplePhoto"

imagePath = os.path.join(currentPath, imageDir)
imageNames = os.listdir(imagePath)
for i,imageName in enumerate(imageNames):
	images = os.path.join(imagePath, imageName)
	print(images)
	img = cv2.imread(images)
	img_darknet = Image(img)
	results = net.detect(img_darknet, thresh = 0.1)
	height = img.shape[0]
	width = img.shape[1]
	for cat, score, bounds in results:

		x, y, w, h = bounds
		classes1 = cat.decode("utf-8")

		xmin = x - w/2
		xmin = round(xmin)
		if (xmin < 0):
			xmin = 0
		ymin = y - h/2
		ymin = round(ymin)
		if (ymin < 0):
			ymin = 0
		xmax = x + w/2
		xmax = round(xmax)
		if (xmax > width):
			xmax = width
		ymax = y + h/2
		ymax = round(ymax)
		if (ymax > height):
			ymax = height
		line1 = line1.lstrip("0")
		cv2.rectangle(img, (int(x - w / 2), int(y - h / 2)), (int(x + w / 2), int(y + h / 2)), (255, 0, 0), thickness=2)

	savingName = os.path.join(savingDirectory, imageName)
	#print (string)
	cv2.imwrite(savingName, img)

finishTime = time.time()
ellapsedTime = finishTime - start_time
fps = i / ellapsedTime

print("FPS = " + str(fps) + "\n" + "Ellapsed Time = " + str(ellapsedTime))