"""
MUST ROBOTICS
Capturing video using Camera
"""
import cv2

video = cv2.VideoCapture(0)

if(video.isOpened() == False):
    print("Failed")

while(True):
    ret, frame = video.read()
    
    cv2.imshow("Video Capturing", frame)
    
    if cv2.waitKey(1) & 0XFF ==ord('q'):
        break
video.release()
cv2.destroyAllWindows()

