#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_1.py
# Measure distance using an ultrasonic module
#
# Author : Matt Hawkins
# Date   : 22/12/2012

# Import required Python libraries
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 24

adjustment = 7

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
while True:
	# Set trigger to False (Low)
	GPIO.output(GPIO_TRIGGER, False)

	# Allow module to settle
	time.sleep(0.5)

	# Send 10us pulse to trigger
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	start = time.time()
	GPIO.output(GPIO_TRIGGER, False)

	while GPIO.input(GPIO_ECHO)==0:
  		stop = time.time()

	while GPIO.input(GPIO_ECHO)==1:
  		stop = time.time()

	# Calculate pulse length
	elapsed = stop-start

	# Distance pulse travelled in that time is time
	# multiplied by the speed of sound (cm/s)
	distance = elapsed * 34300

	# That was the distance there and back so halve the value
	distance = distance / 2

	# Apply adjustment to tweak result
	distance = distance - adjustment

	print "Distance : %.1f" % distance

# Reset GPIO settings
GPIO.cleanup()
