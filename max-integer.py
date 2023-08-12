#!/usr/bin/env python3
# max-integer.py

import random

range = 100
n = 100

updates = 0


def maxinteger(integers: list) -> int:
	"""
	Given a list of integers, determine the maximum value.
	Args:
		integers: list of integers
	Returns:
		integer: maximum value
	"""
	maxvalue = 0
	global updates
	for integer in integers:
		if integer > maxvalue:
			maxvalue = integer
			updates += 1
	return maxvalue


def main():
	random_values = []
	i = 0
	while i < n:
		random_values.append(random.randint(1,range))
		i += 1
	print("Number of integers: %d" % n)
	print("Number of updates: %d" % updates)
	print("Maximum value obtained: %d" % maxinteger(random_values))


if __name__ == "__main__":
	main()