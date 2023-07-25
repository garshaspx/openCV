#
# find object in a photo and mark it
# 
# 
# 
#
#

import cv2
#import numpy as np


cam = cv2.VideoCapture(0)
template_path = 'C:\\Users\\garshasp\\Pictures\\WIN_20230724_13_24_05_Pro.jpg'
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)



template_path1 = 'C:\\Users\\garshasp\\Pictures\\WIN_20230724_13_10_08_Pro.jpg'
template1 = cv2.imread(template_path1, cv2.IMREAD_GRAYSCALE)
list_temp = [template, template1]

threshold = 0.8

# add threshold option
while True:
        
    id, camera = cam.read()
    image = cv2.cvtColor(camera, cv2.COLOR_BGR2GRAY)
        
    for i in list_temp:

        result = cv2.matchTemplate(image, i, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        bottom_right = (max_loc[0] + i.shape[1], max_loc[1] + i.shape[0])
        cv2.rectangle(camera, max_loc, bottom_right, 255, 2)

    print(max_loc, bottom_right)
    cv2.imshow("machted", camera)
    cv2.waitKey(10)
    
    
    """
    #expkain thos code cv2.findNonZero(result, threshold)
    #thresholded_result = cv2.threshold(result, threshold, 1, cv2.THRESH_BINARY)
    result_normalized = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    thresholded_result = cv2.threshold(result_normalized, int(threshold * 255), 255, cv2.THRESH_BINARY)
    print(thresholded_result)
    #locations = np.where(thresholded_result >= threshold)
"""
    
    
    