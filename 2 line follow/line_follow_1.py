import gpiozero
import time

motorLeft = gpiozero.Motor(forward=18, backward=15)
motorRight = gpiozero.Motor(forward=12, backward=16)
sensorRight = gpiozero.LineSensor(20)
sensorLeft = gpiozero.LineSensor(14)
sensorCenter = gpiozero.LineSensor(21)
distanceSensor = gpiozero.DistanceSensor(echo=23, trigger=24, max_distance=5, threshold_distance=0.4)

# lastLocation = "center"
#
# def rightOut():
#     global lastLocation
#     lastLocation = "rightOut"
#
# def leftOut():
#     global lastLocation
#     lastLocation = "leftOut"
#
#
# sensorRight.when_no_line = lambda: rightOut
# sensorLeft.when_no_line = lambda: leftOut

fullSpeed = 1
mediumSpeed = 0.5

def speedStop():
    global fullSpeed
    fullSpeed = 0
    print("in range, stopping")
def speedGo():
    global fullSpeed
    fullSpeed = 1
    print("out of range, continuing")

distanceSensor.when_in_range = speedStop
distanceSensor.when_out_of_range = speedGo

previousRight = 0
previousLeft = 0

while True:
    # print(fullSpeed)
    time.sleep(0.01)


    # print(distanceSensor.distance)
    # if distanceSensor.distance < 0.1:
    #     motorRight.stop()
    #     motorLeft.stop()
    if sensorRight.value == 0 and sensorLeft.value == 0:
        motorRight.forward(fullSpeed)
        motorLeft.forward(fullSpeed)
    elif sensorRight.value == 0 and sensorLeft.value == 1:
        motorRight.forward(fullSpeed)
        motorLeft.stop()
        while sensorCenter.value != 1:
            motorRight.forward(fullSpeed)
            motorLeft.stop()
    elif sensorRight.value == 1 and sensorLeft.value == 0:
        motorRight.stop()
        motorLeft.forward(fullSpeed)
        while sensorCenter.value != 1:
            motorRight.stop()
            motorLeft.forward(fullSpeed)
    else:
        motorRight.forward(fullSpeed)
        motorLeft.forward(fullSpeed)
        # motorRight.stop()
        # motorLeft.stop()
    # previousRight = sensorRight.value
    # previousLeft = sensorLeft.value

