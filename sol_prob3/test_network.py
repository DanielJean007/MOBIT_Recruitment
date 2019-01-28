# USAGE
# python test_network.py --model santa_not_santa.model --image examples/santa_01.png
# python test_network.py --model car_type_classifier.model --image examples/type0-0.png

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
orig = image.copy()

# pre-process the image for classification
image = cv2.resize(image, (28, 28))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network
print("[INFO] loading network...")
model = load_model(args["model"])

# classify the input image
# (notSanta, santa) = model.predict(image)[0]
(type0, type3, type4, type5) = model.predict(image)[0]
# print(type0)
# print(type3)
# print(type4)
# print(type5)

# build the label
if type3 > type0 and type3 > type4 and type3 > type5:
	label = "Type 3"
	proba = type3
elif type4 > type0 and type4 > type3 and type4 > type5:
	label = "Type 4"
	proba = type4
elif type5 > type0 and type5 > type3 and type5 > type4:
	label = "Type 5"
	proba = type5
else:
	label = "Undefined"
	proba = type0
# label = "Undefined" if type0 > notSanta else "Not Santa"
# proba = santa if santa > notSanta else notSanta
label = "{}: {:.2f}%".format(label, proba * 100)
print(label)

# draw the label on the image
output = imutils.resize(orig, width=400)
cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)

# show the output image
# cv2.imshow("Output", output)
cv2.imwrite('result.jpg',output)
# cv2.waitKey(0)