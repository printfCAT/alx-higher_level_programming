#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
	print("{} is negative".format(number))
elif number == 0:
	print("{} is zero".format(number))
else:
	print("{} is positive".format(number))
