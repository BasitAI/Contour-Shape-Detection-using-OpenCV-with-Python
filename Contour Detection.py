# Contours/Shapes Detection
#By implementing contour detection, we can mark the borders of objects,
# and concentrate them in an image with ease.
# Contour detections take a binary image as an input which is the output of the canny edge detector
# or a binary image obtained by applying the global thresholding technique on a grayscale image.
# It calculates the boundaries of objects and makes a hierarchy of the object contours to keep
# the holes inside the parent objects.
# This information can be used to extract and draw any contour depending upon the user requirement.


import cv2
import numpy as np

# Define a function by the Name getContours
def getCorners(img):
    #Using cv2.findContours(image, using external retrieval method to retrieve outer corners)
    contours,hierachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    # See, there are three arguments in cv.findContours() function, first one is source image,
    # second is contour retrieval mode, third is contour approximation method.
    # And it outputs the contours and hierarchy.
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        # Defining Threshold to filter noise
        if area>500:
            # To draw the contours, cv.drawContours function is used.
            # It can also be used to draw any shape provided you have its boundary points.
            # Its first argument is source image, second argument is the contours which should be passed as a Python list
            # third argument is index of contours (useful when drawing individual contour.
            # To draw all contours, pass -1) and remaining arguments are color, thickness etc.
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 6)
            Perimeter = cv2.arcLength(cnt,True)
            print(Perimeter)
            # Approximate Corner points
            approx = cv2.approxPolyDP(cnt,0.02*Perimeter,True)
            print(len(approx))

            objCorner = len(approx)
            # Create a bounding box
            x,y,w,h = cv2.boundingRect(approx)

            if objCorner == 3: objectType = "Triangle"
            elif objCorner == 4:
                Width_by_height_ratio = w/float(h)
                if Width_by_height_ratio > 0.95 and Width_by_height_ratio < 1.05: objectType = "Square"
                else:objectType = "Rectangle"
            elif objCorner>4: objectType = "circle"
            else:objectType="None"


            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),3)
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),
                        cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
# Loading the images from Resources folder and printing it out using imshow function
# To run this code u just need to give a particular path in which your shapes image is stored
Data = 'Resources/shapes.png'
img = cv2.imread(Data)
imgContour = img.copy()
# Convert the image from RGB(BGR in terms of openCV) to GrayScale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Add a little bit blur using Gaussian Blur Function Kernel=(7,7), sigma= 1 represent the amount of blur
Blured_image = cv2.GaussianBlur(imgGray,(7,7),1)
# Detecting Edges Using
imgCanny = cv2.Canny(Blured_image,50,50)
# Function Call
getCorners(imgCanny)

imgBlank = np.zeros_like(img)

cv2.imshow("Original",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",Blured_image)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Blank",imgBlank)
cv2.imshow("Contour",imgContour)

cv2.waitKey(0)