from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep
from datetime import datetime

#a motion sensor(pin4) and the PiCamera
sensor = MotionSensor(4)
camera = PiCamera()

#start the camera
camera.rotation = 180
camera.start_preview()

#take photo when motion is detected
def take_photo():
    global i
    i = i + 1
    camera.capture('/home/michael/pictures/image_%s.jpg' % i)
    print('A photo has been taken')
    sleep(3)

def main():
    while True:
        sensor.wait_for_motion()
        print("detected motion")
        filename = "/var/www/html/photos/MotionDetected_{0:%Y-%m-%d_%H:%M:%S}.jpg".format(datetime.now())
        camera.capture(filename)
        sleep(1)

        sensor.wait_for_no_motion()
        print("no motion detected")
        sleep(1)


if __name__ == "__main__":
    main()
