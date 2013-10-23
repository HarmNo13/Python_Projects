#test git
#!/usr/bin/python
# program of calculator
import os
from Tkinter import *

root=Tk()


def num1(event):		# (num0...num9)
	global s
	s=s+'1'
	os.system('clear')
	print(s)

def num2(event):
	global s
	s=s+'2'	
	os.system('clear')
	print(s)

def num3(event):
	global s
	s=s+'3'	
	os.system('clear')
	print(s)

