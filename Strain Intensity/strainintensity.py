#!/usr/bin/env python

# Setup
import pyautogui
import time
import sys
import re

yellow = False
pyautogui.PAUSE = 0
Ns = int(sys.argv[1])
Nd = int(sys.argv[2])
measurements = 0
sensors = Ns

Nt = int(sys.argv[3])
nums = [Nt]

# Start up MATLAB script
pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
pyautogui.write("strainintensity({}, {})".format(Ns, Nd))
pyautogui.press("enter")
time.sleep(1)


while sensors > 0:
    time.sleep(5)
    # Start up UniVert
    titles = pyautogui.getAllTitles()
    r = re.compile("UniVert.*")
    uni = list(filter(r.match,titles))
    pyautogui.getWindowsWithTitle(uni[0])[0].activate()
    pyautogui.hotkey('ctrl','n')
    pyautogui.press('enter')
    time.sleep(7.5)
    pyautogui.doubleClick(x = 556, y = 187)
    pyautogui.write("98")
    pyautogui.press('enter')
    time.sleep(2.5)
    pyautogui.leftClick(x = 186, y = 81)
    input("Sensor #" + str(Ns - sensors + 1))
    pyautogui.getWindowsWithTitle("Command Prompt")[0].minimize()
    titles = pyautogui.getAllTitles()
    r = re.compile("UniVert.*")
    uni = list(filter(r.match,titles))
    pyautogui.getWindowsWithTitle(uni[0])[0].activate()
    time.sleep(2)
    pyautogui.leftClick(x = 29, y = 96)
    sensors = sensors - 1
    measurements = Nd
    pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
    while measurements > 0:
        # Check if holding
        if not yellow and pyautogui.pixelMatchesColor(525,267,(255,255,0)):
            yellow = True
            pyautogui.press('enter')
            measurements = measurements - 1
        # Check if not holding
        if yellow and pyautogui.pixelMatchesColor(525,267,(255,255,255)):
            yellow = False
    txt = input("Press 'r' to redo: ")
    Nt = Nt + 1
    if txt == 'r':
        pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
        pyautogui.write('r')
        pyautogui.press('enter')
        sensors = sensors + 1
        continue
    else:
        pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
        pyautogui.press('enter')
        nums.append(Nt)

print(nums[0:-2])