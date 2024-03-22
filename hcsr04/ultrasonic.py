import RPi.GPIO as GPIO
import time

# Using broadcom numbering scheme
GPIO.setmode(GPIO.BCM)
# Set GPIO pin numbers for trigger (output) and echo (input)
Trig, Echo = 17, 27
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

# Set GPIO - Trigger to 0V
GPIO.output(Trig, False)
print("Wait: Sensor is settling")
time.sleep(2)

# Create function to calculate distance from an object
def distance():
	GPIO.output(Trig, True)
	time.sleep(0.00001)
	GPIO.output(Trig, False)

	while GPIO.input(Echo) == 0:
		PulseStart = time.time()
	while GPIO.input(Echo) == 1:
		PulseEnd = time.time()

	D = round((PulseEnd-PulseStart)*17000, 3)
	return D

if __name__ == '__main__':
	try:
		print("Start measurements")
		while True:
			dist = distance()
			print("Distance is: ", dist, "cm")
			time.sleep(0.5)
	except KeyboardInterrupt:
		print("Measurements terminated")
		GPIO.cleanup()