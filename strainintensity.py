#!/usr/bin/env python

# Setup
import pyautogui
import time
import sys
import re

pyautogui.PAUSE = 0
yellow = False
Ns = int(sys.argv[1])
Nd = int(sys.argv[2])
measurements = 0
sensors = Ns

Nt = sys.argv[3]

# Start up MATLAB script
pyautogui.getWindowsWithTitle("Command Prompt")[0].minimize()
pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
pyautogui.write("strainintensity({}, {})".format(Ns, Nd))
pyautogui.press("enter")
time.sleep(2)

while sensors > 0:
    # Switch sensors
    if measurements == 0
        input("Sensor #" + str(Ns - sensors + 1))
        sensors = sensors - 1
        measurements = Nd
        # Start up UniVert
        pyautogui.getWindowsWithTitle("UniVert - testrun" + Nt + ".tst")[0].activate()
        pyautogui.hotkey('ctrl','n')
        pyautogui.leftClick(x = 556, y = 187)
        pyautogui.write("98")
        pyautogui.leftClick(x = 186, y = 76)
        time.sleep(5)
        pyautogui.leftClick(x = 29, y = 96)
        pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
        Nt = str(int(Nt) + 1).zfill(3)
    # Check if holding
    if not yellow:
        if pyautogui.pixelMatchesColor(517,282,(255,255,0)):
            yellow = True
            pyautogui.press('enter')
            measurements = measurements - 1
    # Check if not holding
    if yellow:
        if pyautogui.pixelMatchesColor(517,282,(255,255,255)):
            yellow = False