from gpiozero import LED
import time

# The library uses broadcom numbering as default
red = LED(17)
yellow = LED(27)
green = LED(22)
runs = int(input("Enter number of runs"))

for run in range(0,runs):
	try: 
		# Syntax: blink(on_time=1, off_time=1)
		red.blink(on_time=1, off_time=2)
		time.sleep(1)
		yellow.blink(on_time=1, off_time=2)
		time.sleep(1)
		green.blink(on_time=1, off_time=2)
		print("Run number: ",run+1)
		
	except KeyboardInterrupt: # Diagnostic when pressing ctrl+C is avoided: reason for termination is avoided
		break # If signal (ctrl+C) is obtained, terminate loop.