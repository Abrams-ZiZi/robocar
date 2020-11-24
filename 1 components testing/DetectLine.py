from gpiozero import LineSensor
from signal import pause

sensorRight = LineSensor(20)
sensorLeft = LineSensor(14)
sensorRight.when_line = lambda: print('right Line detected')
sensorRight.when_no_line = lambda: print('No right line detected')
sensorLeft.when_line = lambda: print('left Line detected')
sensorLeft.when_no_line = lambda: print('No left line detected')
pause()
