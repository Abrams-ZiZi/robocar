import gpiozero
import time

motorLeft = gpiozero.Motor(forward=18, backward=15)
motorRight = gpiozero.Motor(forward=12, backward=16)
sensorRight = gpiozero.LineSensor(20)
sensorLeft = gpiozero.LineSensor(14)
sensorCenter = gpiozero.LineSensor(21)
distanceSensor = gpiozero.DistanceSensor(echo=23, trigger=24, max_distance=5, threshold_distance=0.4)

speed = 1

def speedStop():
    global speed
    speed = 0
    print("in range, stopping")
def speedGo():
    global speed
    speed = 1
    print("out of range, continuing")

distanceSensor.when_in_range = speedStop
distanceSensor.when_out_of_range = speedGo

while True:
    if sensorRight.value == 0 and sensorLeft.value == 0:
        motorRight.forward(speed)
        motorLeft.forward(speed)
    elif sensorRight.value == 0 and sensorLeft.value == 1:
        motorRight.forward(speed)
        motorLeft.stop()
        while sensorCenter.value != 1:
            motorRight.forward(speed)
            motorLeft.stop()
    elif sensorRight.value == 1 and sensorLeft.value == 0:
        motorRight.stop()
        motorLeft.forward(speed)
        while sensorCenter.value != 1:
            motorRight.stop()
            motorLeft.forward(speed)
    else:
        motorRight.forward(speed)
        motorLeft.forward(speed)

