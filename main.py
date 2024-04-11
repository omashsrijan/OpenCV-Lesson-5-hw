import cv2
import numpy as np
from PIL import Image
import math

# Open colored image in cv2 and Image
img=cv2.imread("happy.jpg",cv2.IMREAD_COLOR)
image = Image.open("happy.jpg")

# Get the width and height of the image
width, height = image.size

# Calculate the pixel size
pixel_size = width * height

# Print the pixel size
print("The pixel size of the image is", pixel_size, "while the width="+str(width)+" & the height="+str(height))

#grayscale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Blur image using 3x3 kernel
gray_blurred=cv2.blur(gray,(3,3))

#Make function to calculate minimum distance(minDist) between detected circles in image.
def detectmindist():
    global mindist
    if width<height:
        mindist=(width)/10
    else:
        mindist=(height)/10
    math.floor(mindist)
    #return mindist
detectmindist()
print(mindist)
#Apply Hough transformation on blurred image, HoughCircles(image, detection method using accumulator, resolution of image<=1, min distance between circle centers, higher threshhold for perfect circle(param1), at least 50% of param1, min radius for detection, max radius for detection)
detected_circles=cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT,1,mindist,param1=50,param2=30,minRadius=1,maxRadius=40)

#Draw Circle
if detected_circles is not None:
    # Convert the circle parameters a, b and r to integers.
    #The value of a (x-coordinate of the center), b (y-coordinate of the center)
    detected_circles=np.uint16(np.around(detected_circles)) #output:[a,b,r] where : represents all indexes
    for i in detected_circles[0,:]:
        a,b,r=i[0],i[1],i[2]
        #draw circumference
        cv2.circle(img,(a,b),r,(0,255,0),2)
        #draw centers
        cv2.circle(img,(a,b),1,(0,0,255),3)
    cv2.imshow("Circle Detection",img)
    cv2.waitKey(0)
cv2.destroyAllWindows()

