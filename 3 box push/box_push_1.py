import gpiozero
import time

motorLeft = gpiozero.Motor(forward=18, backward=15)
motorRight = gpiozero.Motor(forward=12, backward=16)
sensorRight = gpiozero.LineSensor(20)
sensorLeft = gpiozero.LineSensor(14)
sensorCenter = gpiozero.LineSensor(21)
distanceSensor = gpiozero.DistanceSensor(echo=23, trigger=24, max_distance=5)

fullSpeed = 1
mediumSpeed = 0.7

while True:
    while distanceSensor.distance > 0.5:
        motorRight.backward(mediumSpeed)
        motorLeft.stop()
        # motorLeft.forward(mediumSpeed)
        print(distanceSensor.distance)
        time.sleep(0.02)
    print("I see the box")


    # doesn't do anything
    if distanceSensor.distance > 0.5:
        print("accidentally overrun, correcting")
        while distanceSensor.distance > 0.5:
            motorRight.stop()
            motorLeft.forward(mediumSpeed)
            # motorLeft.forward(mediumSpeed)
            print(distanceSensor.distance)
            time.sleep(0.02)


    motorRight.stop()
    motorLeft.stop()
    time.sleep(2)

    motorLeft.backward(0.5)
    time.sleep(0.4)

    print(distanceSensor.distance)

    # motorLeft.backward()
    # time.sleep(0.3)
    # motorLeft.stop()
    # time.sleep(1)

    time1 = time.clock()
    print("First time:", time1)
    print("Pushing box")
    while sensorCenter.value == 0:
        motorRight.forward()
        motorLeft.forward()

    print("Line detected, stopping")
    motorRight.stop()
    motorLeft.stop()
    time.sleep(0.5)
    print("going back to original position")
    motorRight.backward()
    motorLeft.backward()
    time2 = time.clock()
    print("Second time:", time2)
    time.sleep(time2 - (time1 + 0.3))
    motorRight.stop()
    motorLeft.stop()
    time.sleep(0.5)
    motorRight.backward(mediumSpeed)
    motorLeft.stop()
    # motorLeft.forward(mediumSpeed)
    time.sleep(0.5)


