import Adafruit_BMP.BMP085 as BMP085
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)






trig = 17
echo = 27

ir1 = 22
ir2 = 5

led1 = 12
led2 = 16
led3 = 20
led4 = 21

relay1 = 6
relay2 = 13
relay3 = 19
relay4 = 26


GPIO.setup(ir1,GPIO.IN)
GPIO.setup(ir2,GPIO.IN)

GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
GPIO.setup(led4,GPIO.OUT)

GPIO.setup(relay1,GPIO.OUT)
GPIO.setup(relay2,GPIO.OUT)
GPIO.setup(relay3,GPIO.OUT)
GPIO.setup(relay4,GPIO.OUT)

GPIO.output(led1,False)
GPIO.output(led2,False)
GPIO.output(led3,False)
GPIO.output(led4,False)

GPIO.output(relay1,False)
GPIO.output(relay2,False)
GPIO.output(relay3,False)
GPIO.output(relay4,False)

print "ultrasonic measurement"

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

GPIO.output(trig, False)
time.sleep(2)

try:
    while True:

        #BELO CODE FOR ULTRASONIC SENSOR TILL DOUBLE HASH LINES
        GPIO.output(trig,True)
        time.sleep(0.00001)
        GPIO.output(trig,False)
        pulse_end = 0;
        while GPIO.input(echo) == 0:
            pulse_start=time.time()
        
        while GPIO.input(echo) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        #print pulse_duration
        distance = pulse_duration * 17150
        #pulse_end = pulse_end * 1000  * 1000

        #distance = pulse_end / 58       
        distance = round(distance,2)
        print distance
        #########################################################
        #########################################################


        # BELOW CODE FOR IR SENSORS 
        if GPIO.input(ir1) == 0:
            print 'Sensor 1 LOW'
            GPIO.output(led1,True);
            GPIO.output(led2,True);
            GPIO.output(relay1,True);
            GPIO.output(relay2,True);
        else:
            print 'Sensor 1 HIGH'
            GPIO.output(led1,False);
            GPIO.output(led2,False);
            GPIO.output(relay1,False);
            GPIO.output(relay2,False);
        
        if GPIO.input(ir2) == 0:
            print 'Sensor 2 LOW'
            GPIO.output(led3,True);
            GPIO.output(led4,True);
            GPIO.output(relay3,True);
            GPIO.output(relay4,True);
        else:
            print 'Sensor 2 HIGH'
            GPIO.output(led3,False);
            GPIO.output(led4,False);
            GPIO.output(relay3,False);
            GPIO.output(relay4,False);
        time.sleep(1);
        #########################################################
        #########################################################
        
        # BELOW CODE FOR BMP SENSOR
        sensor = BMP085.BMP085()
        print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
        print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())
        print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
        print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())
        #########################################################
        #########################################################

        time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()

 

    
