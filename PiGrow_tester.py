import RPi.GPIO as GPIO
import time
#import sys
#import Adafruit_DHT

#Additional libraries to be used for Adafruit script of the DHT sensor

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup pins 17, 18, and 27 for light, fan and pump respectively
GPIO.setup(17, GPIO.OUT, initial=0)
GPIO.setup(18, GPIO.OUT, initial=0)
GPIO.setup(27, GPIO.OUT, initial=0)

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
#
def tempMeasure():
	#TODO add adafruit code for DHT sensor

def main():
	global_hour = int()
	hourlyLight()

#defining infinite loop
while True:
	main()
	print global_hour #TEST
	#print value from tempMeasure

#figure out way to write the if statement within main()
#prob is keeping the var from one method into the next the same

	if(global_hour >= 6 and global_hour <= 21): #Turn light on
		GPIO.output(17, True)
	else:
		GPIO.output(17, False)

	if(global_hour >= 10 and global_hour <= 12): #Turn fan on
		GPIO.output(18, True)
	else:
		GPIO.output(18, False)
	#write if statement for pump
	time.sleep(3600) #Wait for 3600 secs or 1 hr 
