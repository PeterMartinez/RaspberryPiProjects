#!/usr/bin/python
import time
import datetime
import RPi.GPIO as GPIO
from Adafruit_7Segment import SevenSegment

segment = SevenSegment(address=0x70)

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 24

adjustment = 7

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
  if distance > 99:
    show = int(distance)
    number_string = str(show)

    for i in range(0,4):
      if i != 2:
        segment.writeDigit(i, int(number_string[i]));

  else:
    show = round(distance,2)
    number_string = str(show)    
    if show > 10:
              segment.writeDigit(0, int(number_string[0]));
              segment.writeDigit(1, int(number_string[1]),True);
              segment.writeDigit(3, int(number_string[3]));
              segment.writeDigit(4, int(number_string[4]));
    
  
  # Wait one second
  time.sleep(1)

  # Reset GPIO settings
GPIO.cleanup()
