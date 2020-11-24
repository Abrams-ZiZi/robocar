import gpiozero
import time

motorRight = gpiozero.Motor(forward=18, backward=15)
motorLeft = gpiozero.Motor(forward=12, backward=16)

while True:
    print("Motor spinning forward.")
    motorRight.forward()
    motorLeft.forward()
    time.sleep(5)
    motorRight.stop()
    motorLeft.stop()
    time.sleep(3)
    print("Motor spinning backward.")
    motorRight.backward()
    motorLeft.backward()
    time.sleep(5)
    motorRight.stop()
    motorLeft.stop()
    time.sleep(3)
