import RPi.GPIO as GPIO
import time

# Setting GPIO pin numbering schemes:
GPIO.setmode(GPIO.BCM) # Allows for broadcom numbering schemes
# GPIO.setmode(GPIO.BOARD) # Allows for board numbering schemes

pin_output = 17

# Set gpio pin 17 as output
GPIO.output(pin_output,GPIO.OUT)
# Define high and low for LED blinking
On, Off = 1, 0
sleepy = 0.1
cont = True

while cont:
    blinks = int(input("Enter the number of blinks: "))
    print("Start blinking")
    for blink in range(0,blinks):
        GPIO.output(pin_output, On)
        time.sleep(sleepy)
        GPIO.output(pin_output, Off)
        print("Iteration: ", blink)
    
    cont = bool(input("Enter 1 to continue and 0 to terminate"))

print("The LED has blinked ", blinks, " times.")
# Release all pins for next program:
GPIO.cleanup()


