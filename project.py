# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pins 11 & 12 as outputs, and define as PWM servo1 & servo2
GPIO.setup(11,GPIO.OUT)
servo2 = GPIO.PWM(11,50) # pin 11 for servo1
GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(12,50) # pin 12 for servo2

# Start PWM running on both servos, value of 0 (pulse off)
servo1.start(0)
servo2.start(0)

servo2.ChangeDutyCycle(2)
servo1.ChangeDutyCycle(2)
time.sleep(0.5)
servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)

def print_menu():
	print("Select a command:")
	print("	1. Switch to the other servo")
	print("	2. Turn the servo 90 degrees clockwise")
	print("	3. Turn the servo back to 0")
	print(" 0. Exit")
	
def turn_clockwise_90(servo):
	servo.ChangeDutyCycle(7)
	time.sleep(0.5)
	servo.ChangeDutyCycle(0)
	

def turn_to_0(servo):
	servo.ChangeDutyCycle(2)
	time.sleep(0.5)
	servo.ChangeDutyCycle(0)
	
current_servo = servo1

while True:
	print_menu()
	cmd = int(input(">>>"))
	
	if cmd == 0: 
		break
	if cmd == 1:
		if current_servo == servo1:
			current_servo = servo2
			print("Current servo is set to servo 2")
		else:
			current_servo = servo1
			print("Current servo is set to servo 1")
	if cmd == 2:
		turn_clockwise_90(current_servo)
	if cmd == 3:
		turn_to_0(current_servo)
		

#Clean things up at the end
servo1.stop()
servo2.stop()
GPIO.cleanup()

print ("Goodbye")
