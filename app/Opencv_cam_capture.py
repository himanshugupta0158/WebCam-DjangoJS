import cv2 as cv
import time

capture = cv.VideoCapture(0)
count = 0 

start_time = int(time.time())



while True:
    isTrue, frame = capture.read()
    key = cv.waitKey(1)

    cv.imshow("Cam Video",frame)

    if key == ord('q'):
        break

    
    current_time = int(time.time())
    
    isTenSec = current_time - start_time

    if isTenSec >= 10:
        start_time = current_time
        print("Time difference : ",isTenSec)
        if count == 0:
            name = f'app/images/saved_img.jpg'
            count += 1
        else:
            name = f'app/images/saved_img{count}.jpg'
            count += 1
        cv.imwrite(filename=str(name), img=frame)

    

    
    
    # capture.release()

capture.release()
cv.destroyAllWindows()