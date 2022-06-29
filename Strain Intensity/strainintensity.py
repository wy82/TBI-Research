#!/usr/bin/env python

# Setup
import pyautogui
import time
import sys
import re

pyautogui.PAUSE = 0
Ns = int(sys.argv[1])
Nc = int(sys.argv[2])
Nd = int(sys.argv[3])
measurements = 0
cycles = Nc*Ns

Nt = int(sys.argv[4])
name = sys.argv[5]
nums = []

# Start up MATLAB script
pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
pyautogui.write("strainintensity({}, {}, {}, '{}')".format(Ns, Nc, Nd, name))
pyautogui.press("enter")

while cycles > 0:
    time.sleep(1)
    # Start up UniVert
    titles = pyautogui.getAllTitles()
    r = re.compile("UniVert.*")
    uni = list(filter(r.match,titles))
    pyautogui.getWindowsWithTitle(uni[0])[0].activate()
    # Create new test
    pyautogui.hotkey('ctrl','n')
    pyautogui.press('enter')
    time.sleep(6)
    # Reset displacement
    pyautogui.doubleClick(x = 556, y = 187)
    pyautogui.write("98")
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.leftClick(x = 186, y = 81)
    time.sleep(4)
    # Wait for input to start
    if cycles % Nc == 0:
        input("Sensor #" + str((Nc*Ns - cycles)//Nc + 1))
        pyautogui.getWindowsWithTitle("Command Prompt")[0].minimize()
        titles = pyautogui.getAllTitles()
        r = re.compile("UniVert.*")
        uni = list(filter(r.match,titles))
        pyautogui.getWindowsWithTitle(uni[0])[0].activate()
    time.sleep(1)
    cycles = cycles - 1
    measurements = Nd
    # Start test
    pyautogui.leftClick(x = 29, y = 96)
    pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(21)

    if cycles % Nc == 0:
        txt = input("Press 'r' to redo: ")
        # Continue
        if txt != 'r':
            pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
            pyautogui.press('enter')
            nums.append(Nt-4)
        # Redo
        else: 
            pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
            pyautogui.write('r')
            pyautogui.press('enter')
            cycles = cycles + Nc
    Nt = Nt + 1
# Print test run numbers
print(nums)