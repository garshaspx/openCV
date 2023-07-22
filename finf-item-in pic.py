#
# 
# 
# 
#track item in a picture
# 
#

#import cv2

"""
from PIL import Image
from rembg import remove
def back_remover():
        im = Image.open(template_path)
        noback = remove(im)
        bg = Image.new("RGB", noback.size, (255, 255, 255))
        bg.paste(noback, noback)
        bg.save(template_path)
back_remover()
"""



"""

cam = cv2.VideoCapture(0)
template_path = 'C:\\Users\\garshasp\\Pictures\\WIN_20230721_12_44_48_Pro.jpg'
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)


    
    
while True:

    id, camera = cam.read()
    image = cv2.cvtColor(camera, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(image, template, cv2.TM_CCORR)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    bottom_right = (max_loc[0] + template.shape[1], max_loc[1] + template.shape[0])
    cv2.rectangle(camera, max_loc, bottom_right, 255, 2)
    cv2.imshow('Matched Item', camera)
    if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break"""
    
    
    
    
    
    
    







import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('C:\\Users\\garshasp\\Pictures\\WIN_20230721_12_44_48_Pro.jpg', cv.IMREAD_GRAYSCALE)

img2 = img.copy()

cam = cv.VideoCapture(0)
id, template = cam.read()
templateg = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
#template = cv.imread('template.jpg', cv.IMREAD_GRAYSCALE)


w, h, adx = template.shape[::-1]
# All the 6 methods for comparison in a list

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR','cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()

