import numpy as np
import cv2
file_path = ""
img_name = 'txt_mudit_b8_1_742'
mask = cv2.imread(file_path+img_name + '.jpg')



for i in range(mask.shape[0]):
    for j in range(mask.shape[1]):
        if(mask[i,j,0]>250 or mask[i,j,1]>250 or mask[i,j,2]>250):
            mask[i,j,2]=0
            mask[i,j,1]=0
            mask[i,j,0]=0
        else:
            mask[i,j,2]=255
            mask[i,j,1]=255
            mask[i,j,0]=255
            
for i in range(mask.shape[0]):
    for j in range(mask.shape[1]):
        if(mask[i,j,0]==255 or mask[i,j,1]==255 or mask[i,j,2]==255):
            mask[i,j,2]=0
            mask[i,j,1]=0
            mask[i,j,0]=0
        else:
            mask[i,j,2]=255
            mask[i,j,1]=255
            mask[i,j,0]=255
        
img = cv2.imread(file_path+img_name + '.jpg')

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)

img2 = cv2.inpaint(img, mask, 15, cv2.INPAINT_NS)

cv2.imwrite('mask_' + img_name+'.jpg',mask)