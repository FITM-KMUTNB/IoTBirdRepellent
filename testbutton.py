import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time


def button_callback(channel):
    print("Button was pushed!")
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(5,GPIO.RISING,callback=button_callback) # Setup event onpin 10 rising edge
while(1):
    print("Hello")
    time.sleep(1)
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
 
