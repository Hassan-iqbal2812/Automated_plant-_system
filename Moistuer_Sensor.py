import RPi.GPIO as GPIO
from gpiozero import LED
import time

from time import gmtime,strftime

print("STARTING")




channel=21
motor = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)


def Testfunc(channel):
	if GPIO.input(channel):
		print("NO Moisture Detected")
		print(strftime("%Y-%m-%d %H:%M:%s",gmtime()))
		GPIO.setup(motor,GPIO.OUT)
		#GPIO.output(motor,GPIO.HIGH)
		print("TURNING MOTOR ON")
		time.sleep(2)
		#GPIO.output(motor,GPIO.LOW)
		#GPIO.cleanup()
		print("RED LED on")
		#green_led.off()
		#red_led.on()

	else:
		print("Moisture Detected")
		print(strftime("%Y-%m-%d %H:%M:%s",gmtime()))
		print("GREEN LED on")
		#GPIO.cleanup()
		#red_led.off()
		#green_led.on()

GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=100)
GPIO.add_event_callback(channel,Testfunc)

while True:
	time.sleep(0.1)
