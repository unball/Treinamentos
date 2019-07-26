import cv2

def show(imageBW, mask, image):
	cv2.imshow("Shapes JPG BW", imageBW)
	cv2.imshow("Shapes JPG Thresholded", mask)
	cv2.imshow("Shapes JPG RGB", image)
	cv2.waitKey(0)

# Open image
image = cv2.imread("shapes.jpg")

# Convert to grayscale
imageBW = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Binarize
ret, mask = cv2.threshold(imageBW, 230, 255, cv2.THRESH_BINARY_INV)

# Find contours of interest regions
_,contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
for contour in contours:
	M = cv2.moments(contour)
	x = int(M['m10']/M['m00'])
	y = int(M['m01']/M['m00'])
	perimetro = cv2.arcLength(contour, True)
	points = cv2.approxPolyDP(contour, 0.04*perimetro, True)
	cv2.putText(image, str(len(points)), (x,y), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0))
	cv2.drawContours(image, points, -1, (0,0,0), 4)

#cv2.drawContours(image, contours, -1, (0,0,0), 4)

# Show
show(imageBW, mask, image)
