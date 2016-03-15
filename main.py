import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread("Test Images/img.png",cv2.IMREAD_GRAYSCALE)
# canvas = np.zeros(img[::1],np.uint8)
_ , thresholded_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# thresholded_img = cv2.adaptiveThreshold(img,0,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# edges = cv2.Canny(img,0,255)
# print str(thresholded_img.shape) + str(thresholded_img.dtype)
contour_img = np.zeros(img.shape,np.uint8)
erosion_kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(thresholded_img, erosion_kernel, iterations = 1)
contour,hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(contour_img,contour,-1,(255,0,0),2)

# i = 0
# while not cv2.waitKey() == ord('q') and i < len(contour):
# 	erosion = cv2.erode(contour_img, erosion_kernel, iterations = 1)
# 	cv2.drawContours(contour_img,contour,i,(255,0,0),2)
	# erosion_kernel = np.ones((3,3),np.uint8)
# 	print type(contour)
# 	# for point in contour[i]
# 	# 	print point
# 	cv2.imshow("Eroded",erosion)
# 	cv2.waitKey(0)
# 	i+=1

# cv2.imshow("Original",img)
# cv2.imshow("contour",contour_img)
# cv2.imshow("Eroded",erosion)
# cv2.waitKey(0)

plt.subplot(121),plt.imshow(erosion,cmap='gray'),plt.title("Eroded")
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(contour_img, cmap = 'gray'),plt.title("Contours")
# plt.xticks([]),plt.yticks([])
plt.show()

#--------- TEST CODES ---------
# img = img[:,:,::-1]

# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# laplacian = cv2.Laplacian(img,cv2.CV_64F)
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize = 5)
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize = 5)

# plt.subplot(221), plt.imshow(img, cmap='gray'),plt.title('original')
# plt.xticks([]),plt.yticks([])
# plt.subplot(222), plt.imshow(laplacian, cmap='gray'),plt.title('Laplacian')
# plt.xticks([]),plt.yticks([])
# plt.subplot(223), plt.imshow(sobelx, cmap='gray'),plt.title('Sobel X')
# plt.xticks([]),plt.yticks([])
# plt.subplot(224), plt.imshow(sobely, cmap='gray'),plt.title('Sobel Y')
# plt.xticks([]),plt.yticks([])
# plt.show()

