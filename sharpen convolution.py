import numpy as np
import cv2
file_path = ""
img_name = 'txt_mudit_b8_1_742'


img = cv2.imread(file_path+img_name + '.jpg')


sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
img3 = cv2.filter2D(img, -1, sharpen_kernel)

cv2.imshow('img',img3)
cv2.waitKey(0)
cv2.DestroyAllWindows
