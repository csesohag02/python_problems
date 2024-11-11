"""
Created on Tue Nov 12 01:37:54 2024
@author: csesohag02
"""


import pyautogui as pg
import time

msg = input("Write the message you want to send: ")
n = int(input("How many times want to send the message: "))

time.sleep(8)
for i in range(n):
	pg.write(msg)
	pg.press('enter')

