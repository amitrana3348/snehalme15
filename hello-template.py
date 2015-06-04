from flask import Flask, render_template
import Adafruit_BMP.BMP085 as BMP085
import time
import datetime
import sys

#From this
import RPi.GPIO as GPIO, time, os
DEBUG = 1;
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
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

GPIO.output(trig, False)
time.sleep(2)
countvalue = 0;
#upto this



bmp = BMP085.BMP085()

app = Flask(__name__)

@app.route('/SENS.csv',methods=['GET','POST'])
def textf():
	error = None
	myfile = open("SENS.txt ","r")
	strg = myfile.read()
	myfile.close()
	#response = make_response(csv)
	#response.header["Content-Disposition"]= "attachment;filename=sens.csv"
	return strg
	#return strg

@app.route("/r4on",methods=['GET','POST'])
def hello4():
	GPIO.output(relay4,GPIO.HIGH)
	GPIO.output(led4,True)
	return "relay 4 turned on"


@app.route("/r4off",methods=['GET','POST'])
def hello5():
	GPIO.output(relay4,GPIO.LOW)
	GPIO.output(led4,False)	
	return "relay 4 turned off"

@app.route("/r3on",methods=['GET','POST'])
def hello6():
	GPIO.output(relay3,GPIO.HIGH)
	GPIO.output(led3,True)
	return "relay 3 turned on"
@app.route("/r3off",methods=['GET','POST'])
def hello7():
	GPIO.output(relay3,GPIO.LOW)
	GPIO.output(led3,False)	
	return "relay 3 turned off"

@app.route("/r2on",methods=['GET','POST'])
def hello21():
	GPIO.output(relay2,GPIO.HIGH)
	GPIO.output(led2,True)
	return "relay 2 turned on"

@app.route("/r2off",methods=['GET','POST'])
def hello22():
	GPIO.output(relay2,GPIO.LOW)
	GPIO.output(led2,False)	
	return "relay 2 turned off"

@app.route("/r1on",methods=['GET','POST'])
def hello2():
	GPIO.output(relay1,GPIO.HIGH)
	GPIO.output(led1,True)
	return "relay 1 turned on"
@app.route("/r1off",methods=['GET','POST'])
def hello3():
	GPIO.output(relay1,GPIO.LOW)
	GPIO.output(led1,False)	
	return "relay 1 turned off"

@app.route("/")
def hello():
    global countvalue
    tempr = "%.2f c" % bmp.read_temperature()
    pressure = "%.2f hPa" %bmp.read_pressure()
    altitude = "%.2f m" %bmp.read_altitude()
    
    # IR SENSOR CODE HERE 
    if GPIO.input(ir1) == 0:
		countvalue = countvalue+1
		
    if GPIO.input(ir2) == 0:
		countvalue = countvalue-1
		
    if countvalue < 0:
		countvalue = 0;
    ############# ULTRASONIC CODE BELO
    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)
    pulse_end = 0
    while GPIO.input(echo)==0:
		pulse_start = time.time()
    while GPIO.input(echo) == 1:
		pulse_end = time.time()
    pulse_duration = pulse_end-pulse_start
    distance = pulse_duration * 17150
    distance = round(distance,2)
    #######################################################################3
    #########################################################################
    now = datetime.datetime.now()
    timeString = now.strftime("%d-%m-%Y %H:%M")
    text_file = open("SENS.txt","a")
    text_file.write(timeString + str(tempr) + str(pressure) + str(altitude) + str(countvalue) + str(distance) + '\n\r\r\n')
    text_file.write("\r")
    text_file.close()
    csvfile = open("SENS.csv","a")
    csvfile.write(timeString + ',' + str(tempr) + ',' + str(pressure) + ',' + str(altitude) + ',' + str(countvalue) + ',' + str(distance) + '\r\n\r\n')
    csvfile.close()
    templateData = {
        'title' : 'HELLO!',
        'time' : timeString,
        'temp' :tempr,
        'pres' :pressure,
        'alt' : altitude,
        'cnt' : countvalue,
        'intens' : distance#this is ultrasonic sensor value
        }
    return render_template('main2.html',**templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    
