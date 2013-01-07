#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import datetime as dt
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.output(12, False)
while True:
   time.sleep(2)
   GPIO.output(12, True)
   time.sleep(0.00001)
   GPIO.output(12, False)
   while GPIO.input(11)==False:
      a=1
   t1=dt.datetime.now()
   while GPIO.input(11):
      a=1
   t2=dt.datetime.now()
   t3=(t2-t1).microseconds
   distance=t3/58
   print'Distance:',distance,'cm'
