import random
import time

def DoSomething():
	n = int(input())
	a = [int(input()) for _ in range(n)]
	days = n

	for index, benefit in enumerate(a):
		if days == index+1:
			break
		if benefit == a[index+1]:
			print("stay")
		elif benefit < a[index+1]:
			print("up ", a[index+1] - benefit)
		elif benefit > a[index+1]:
			print("down ", benefit - a[index+1])

DoSomething()

