import RPi.GPIO as GPIO
import time

channel = 20
channel2 = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.OUT)
GPIO.setup(channel2,GPIO.OUT)


def turn_motor_on(pin,pin2):
	GPIO.output(pin,GPIO.HIGH) # turns motor on
	GPIO.output(pin2,GPIO.HIGH)
	print("TURNING MOTOR ON")

def turn_motor_off(pin,pin2):
	GPIO.output(pin,GPIO.LOW) #turns motor off
	GPIO.output(pin2,GPIO.LOW)
	print("TURNING MOTOR OFF")

if __name__ == '__main__':
	try:
		turn_motor_off(channel,channel2)
		time.sleep(2)
		turn_motor_on(channel,channel2)
		time.sleep(2)
		GPIO.cleanup()
	except:
		print("ERROR")
		GPIO.cleanup()
