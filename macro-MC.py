# coding: utf-8

from pynput.mouse import Button, Controller
import time
mouse = Controller()

num = input("how much clicks ? >>> ")

def oFunction(num):
	for enum in range(1,int(num) + 1):
		time.sleep(0.1)
		print("[*] " + str(enum) + " clicks")

print("options = attack,build")
option = input('choose option >>> ')
if option == "attack":
	mouse.click(Button.left, int(num))
	oFunction(num)

if option == "build":
	mouse.click(Button.right, int(num))
	oFunction(num)
