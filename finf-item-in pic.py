#
# 
# 
# 
#track item in a picture
# 
#

import cv2

cam = cv2.VideoCapture(0)
template_path = 'C:\\Users\\garshasp\\Pictures\\Camera Roll\\WIN_20230721_12_27_31_Pro.jpg'



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

template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)


    
    
while True:
        
    id, camera = cam.read()
    image = cv2.cvtColor(camera, cv2.COLOR_BGR2GRAY)
    
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    bottom_right = (max_loc[0] + template.shape[1], max_loc[1] + template.shape[0])

    
    cv2.rectangle(camera, max_loc, bottom_right, 255, 2)
    cv2.imshow('Matched Item', camera)
    if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break
    
    
    
    