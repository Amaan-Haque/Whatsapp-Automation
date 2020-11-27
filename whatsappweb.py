from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import *
import requests
import time
from pynput.keyboard import Key, Controller
import sys
import urllib.parse

#Dictionary contains names and numbers key-values

# %20 in times for url encoded space
times = []
names = []
numbers = []
endpoints = []
directory = {}

#Opens the page to scan qr and use whatsapp
def login():
	print("Login using QR code. Press enter when done!")
	driver.get("https://web.whatsapp.com")
	input()

def take_numbers(n):
	print("Enter the numbers with country code (Without '+'): ")
	for i in range(n):
		number = input().strip()
		number = number.replace(" ", "")
		numbers.append(number)

def make_endpoints(encoded_text):
	#Takes dictionary and converts them to end points to make a list
	for number in numbers:
		end_point = '''window.open("https://web.whatsapp.com/send?phone=%2B'''+number+"&text="+encoded_text+'''&app_absent=0");'''
		endpoints.append(end_point)

def send_messages():
	#Iterates through list to send each message
	for url in endpoints:
		driver.execute_script(url)
		time.sleep(8)
		keyboard = Controller()
		keyboard.press(Key.enter)
		time.sleep(0.5)
		keyboard.release(Key.enter)
		time.sleep(1)

def timer_display(n):
	for remaining in range(n, 0, -1):
	    sys.stdout.write("\r")
	    sys.stdout.write(f"{remaining} seconds remaining.") 
	    sys.stdout.flush()
	    time.sleep(1)
	print("\n")
		


# driver
driver = webdriver.Firefox()
login()
n = int(input("Enter number of recepients: "))
text = input("Enter the message to be sent")
encoded_text = urllib.parse.quote(text)
take_numbers(n)
directory = dict(zip(names, numbers))
make_endpoints(encoded_text)
print("Please switch to browser window in 5 secs")
timer_display(5)
send_messages()

