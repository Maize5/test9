#!/usr/bin/env python3
import sys

input_minutes = int(sys.argv[1])
def Hours(input_minutes):
	if input_minutes < 0:
		raise ValueError("Input number connaot be negative")
	else:

		changetime_hour = input_minutes // 60
		changetime_minute = input_minutes % 60
		print("%dH, %dM"%(changetime_hour, changetime_minute))

try:
	Hours(input_minutes)
except ValueError:
	print("Parameter Error")
