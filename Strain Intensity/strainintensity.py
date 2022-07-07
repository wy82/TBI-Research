#!/usr/bin/env python

# Setup
import pyautogui
import time
import sys
import re
import PySimpleGUI as sg

pyautogui.PAUSE = 0
Ns = int(sys.argv[1])
Nc = int(sys.argv[2])
Nd = int(sys.argv[3])
measurements = 0
cycles = Nc*Ns

Nt = int(sys.argv[4])
name = sys.argv[5]
nums = []

# Theme

default = ('Helvetica', 12)
sg.theme('TanBlue')

# Layout

column = [
    [
        sg.Text("Number of Sensors: "),
        sg.In(size =(25,1), enable_events=True, key = "Ns"),
        sg.Text("Number of Cycles: "),
        sg.In(size =(25,1), enable_events=True, key = "Nc"),
        sg.Text("Number of Displacements: "),
        sg.In(size =(25,1), enable_events=True, key = "Nd"),
        sg.Text("Test Run Number: "),
        sg.In(size =(25,1), enable_events=True, key = "Nt"),
        sg.Text("Save As: "),
        sg.In(size =(25,1), enable_events=True, key = "name"),
    ]
]

layout = [
    [sg.Column(column, vertical_alignment = "center")],
    [sg.Button('Begin Test')]
]

# Window

window = sg.Window('Discrepancy Reporter', layout, grab_anywhere = True, size = (350,100), element_justification = 'c', font = default)

# Start up MATLAB script
pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
pyautogui.write("strainintensity({}, {}, {}, '{}')".format(Ns, Nc, Nd, name))
pyautogui.press("enter")

while cycles > 0:
    time.sleep(3)
    # Start up UniVert
    titles = pyautogui.getAllTitles()
    r = re.compile("UniVert.*")
    uni = list(filter(r.match,titles))
    pyautogui.getWindowsWithTitle(uni[0])[0].activate()
    # Create new test
    pyautogui.leftClick(x = 60, y = 96)
    time.sleep(2)
    pyautogui.hotkey('ctrl','n')
    pyautogui.press('enter')
    time.sleep(8)
    # Reset displacement
    pyautogui.doubleClick(x = 186, y = 81)
    time.sleep(8)
    # Wait for input to stat
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
            nums.append(Nt-Nc+1)
        # Redo
        else: 
            pyautogui.getWindowsWithTitle("MATLAB R2022a - academic use")[0].activate()
            pyautogui.write('r')
            pyautogui.press('enter')
            cycles = cycles + Nc
    Nt = Nt + 1
# Print test run numbers
print(nums)