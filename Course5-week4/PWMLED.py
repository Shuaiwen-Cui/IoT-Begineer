#import libraries
import RPi.GPIO as GPIO
import time
#LED on my board
led = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
#50Hz PWM frequency
p = GPIO.PWM(led,100)
#zero brightness, 0% duty cycle
p.start(0)
try:
    while True:
        for i in range(0,100,1): 
         p.ChangeDutyCycle(i)
         time.sleep(0.01)
        for i in range(100, 0, -1): #Changes PWN 100 to 0 by -1.
         p.ChangeDutyCycle(i)
         time.sleep(0.01)
    
except KeyboardInterrupt:  #For shutting the program using keyboard.
    print("Error occurs")
    pass
    