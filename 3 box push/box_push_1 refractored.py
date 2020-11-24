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
lowSpeed = 0.5

while True:
    while distanceSensor.distance > 0.8:
        motorRight.backward(mediumSpeed)
        motorLeft.stop()
        time.sleep(0.02)
    print("I see the box")

    motorRight.stop()
    motorLeft.stop()
    time.sleep(2)
	
	if distanceSensor.distance > 0.8:
        print("accidentally overrun, correcting")
        while distanceSensor.distance > 0.8:
            motorRight.stop()
            motorLeft.forward(lowSpeed)
            time.sleep(0.02)
	else:
		motorLeft.backward(lowSpeed)
		time.sleep(0.4)
		
	motorRight.stop()
    motorLeft.stop()
    time.sleep(1)

    time1 = time.clock()
    print("First time:", time1)
    print("Pushing box")
    while sensorCenter.value == 0:
        motorRight.forward(fullSpeed)
        motorLeft.forward(fullSpeed)
    print("Line detected, stopping")
    motorRight.stop()
    motorLeft.stop()
    time.sleep(0.5)
	time2 = time.clock()
    print("going back to original position")
    motorRight.backward(fullSpeed)
    motorLeft.backward(fullSpeed)
    print("Second time:", time2)
    time.sleep(time2 - (time1 + 0.3))
    motorRight.stop()
    motorLeft.stop()
    time.sleep(0.5)
	
    motorRight.backward(mediumSpeed)
    motorLeft.stop()
    time.sleep(0.5)


