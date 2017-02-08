import RPi.GPIO as GPIO
import time
import sys
import Adafruit_DHT

#Additional libraries to be used for Adafruit script of the DHT sensor

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup pins 17, 18, and 27 for light, fan and pump respectively
GPIO.setup(17, GPIO.OUT, initial=0)
GPIO.setup(18, GPIO.OUT, initial=0)
#GPIO.setup(27, GPIO.OUT, initial=0)

#Setup DHT sensor
def tempMeasure():
	sensor = Adafruit_DHT.DHT11
	pin = 22 #TEST
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
		print 'Temp={0:0.1f}*C \nHumidity={1:0.1f}%'.format(temperature, humidity)
	else:
		print 'Failed to get reading, Try again!'


#Start setting up Threads at some point to deal with the various tasks....
def hourlyLight():
	localtime = time.asctime( time.localtime(time.time() ))
	localtime = localtime.split(" ")
	timer = localtime[-2] #workaround for empty string in localtime CBTT!
	timer = timer.split(":")
	hour = timer[0]
	global global_hour
	global_hour = int(hour)
	#print global_hour #TEST global var

def main():
	global_hour = int()
	hourlyLight()

#defining infinite loop
while True:
	main()
	print global_hour #TEST
	tempMeasure()
	#print value from tempMeasure

#figure out way to write the if statement within main()
#prob is keeping the var from one method into the next the same

	if(global_hour >= 6 and global_hour <= 21): #Turn light on
		GPIO.output(17, True)
	else:
		GPIO.output(17, False)

	if(global_hour == 10): #Turn fan on
		GPIO.output(18, True)
	else:
		GPIO.output(18, False)
	#write if statement for pump
	time.sleep(900) #Wait for 3600 secs or 1 hr 
