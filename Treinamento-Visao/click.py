import cv2
import numpy as np

def cut(image, clicks):
	return image[clicks[0][1]:clicks[1][1],clicks[0][0]:clicks[1][0]]

def mouse(evento, x, y, flag, parametros):
	image, mask, clicks = parametros
	img = image.copy()
	if(evento == cv2.EVENT_LBUTTONDOWN):
		if(len(clicks) >= 2): clicks.clear()
		clicks.append((x,y))
		print(clicks)
		if(len(clicks) == 2):
			template = cut(mask, clicks)
			res = cv2.matchTemplate(mask, template, cv2.TM_CCOEFF_NORMED)
			cv2.imshow("Result", res)
			loc = np.where(res>=0.8)
			w, h  = template.shape[:2]
			for pt in zip(*loc[::-1]):
				cv2.rectangle(img, pt, (pt[0] + h, pt[1]+w), (0,0,0), 1)
			cv2.imshow("Shapes JPG RGB", img)
# Open image

image = cv2.imread("letters.png")

# Convert to grayscale
imageBW = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Binarize
ret, mask = cv2.threshold(imageBW, 200, 255, cv2.THRESH_BINARY_INV)

# Show Image

cv2.imshow("Shapes JPG RGB", image)
# Show mask Image
cv2.imshow("Shapes JPG mask", mask)

# Create mouse callback that stores two mouse clicks
clicks = []
cv2.setMouseCallback("Shapes JPG RGB", mouse, (image,mask,clicks))


# Lock
cv2.waitKey(0)
