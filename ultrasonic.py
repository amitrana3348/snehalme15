import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

trig = 23
echo = 24
print "ultrasonic measurement"

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

GPIO.output(trig, False)
time.sleep(2)

try:
    while True:
        GPIO.output(trig,True)
        time.sleep(0.00001)
        GPIO.output(trig,False)
        pulse_end = 0;
        while GPIO.input(echo) == 0:
            pulse_start=time.time()
        
        while GPIO.input(echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        print pulse_duration
        distance = pulse_duration * 17150
        #pulse_end = pulse_end * 1000  * 1000

        #distance = pulse_end / 58       
        distance = round(distance,2)
        print distance
        
        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()

 

    
