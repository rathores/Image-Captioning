import cv2
import os
import time

def Capture_Image():
    camera = cv2.VideoCapture(0)
    if not os.path.exists('Images'):
        os.mkdir('Images')
    while True:
        return_value,image = camera.read()
    #for gray style image
    #gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Image Captioning',image)
    #To capture image and exit
        if cv2.waitKey(1)& 0xFF == ord('s'):
            tm = time.strftime('%H-%M-%S')
            cv2.imwrite('Images/'+tm+'.jpg',image) 
            break
    camera.release()
    cv2.destroyAllWindows()
    image_path = "Images/"+tm+".jpg"
    return (image_path)
if __name__ == '__main__':
    Capture_Image()
