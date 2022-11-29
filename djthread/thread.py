import threading
from .models import Student
import time
import cv2 as cv
from faker import Faker
import random

fake = Faker()

class CreateStudentThead(threading.Thread):

    def __init__(self, total):
        self.total = total
        threading.Thread.__init__(self)

    def run(self):
        try:
            print('Threading execution started')
            count = 100
            for i in range(self.total):
                print(i)
                Student.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(20, 30)
                )
        except Exception as e:
            print(e)


class SaveCamPic(threading.Thread):

    def __init__(self):
        self.capture = cv.VideoCapture(0)
        self.count = 0

        self.start_time = int(time.time())
        threading.Thread.__init__(self)

    def run(self):
        while True:
            isTrue, frame = self.capture.read()
            key = cv.waitKey(1)

            cv.imshow("Cam Video", frame)

            if key == ord("q"):
                break

            current_time = int(time.time())

            isTenSec = current_time - self.start_time

            if isTenSec >= 5:
                self.start_time = current_time
                print("Time difference : ", isTenSec)
                if self.count == 0:
                    name = f"app/images/saved_img.jpg"
                    self.count += 1
                else:
                    name = f"app/images/saved_img{self.count}.jpg"
                    self.count += 1
                cv.imwrite(filename=str(name), img=frame)


        self.capture.release()
        cv.destroyAllWindows()