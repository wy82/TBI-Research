#!/usr/bin/env python

# Setup
import pyautogui
import time
import re
import PySimpleGUI as sg
import numpy as np

# Theme
default = ('Helvetica', 15)
sg.theme('tanblue')
bgcolor = sg.theme_background_color()

# Layout
column = [
    [
        sg.Text('# of Sensors: '),
    ],
    [
        sg.Text('# of Cycles: '),
    ],
    [
        sg.Text('# of Displacements: '),
    ],
    [
        sg.Text('Test Run #: '),
    ],
    [
        sg.Text('Max Displacement: '),
    ],
    [
        sg.Text('Save As: '),
    ]
]
inputcol = [
    [
        sg.In(size = (10,1), enable_events=True, key = 'Ns'),
        sg.Text(size = (14, 1), font=('Helvetica', 9), justification='center', text_color = 'red', key='Nstext')
    ],
    [
        sg.In(size = (10,1), enable_events=True, key = 'Nc'),
        sg.Text(size = (14, 1), font=('Helvetica', 9), justification='center', text_color = 'red', key='Nctext')
    ],
    [
        sg.In(size = (10,1), enable_events=True, key = 'Nd'),
        sg.Text(size = (14, 1), font=('Helvetica', 9), justification='center', text_color = 'red', key='Ndtext')
    ],
    [
        sg.In(size = (10,1), enable_events=True, key = 'Nt'),
        sg.Text(size = (14, 1), font=('Helvetica', 9), justification='center', text_color = 'red', key='Nttext')
    ],
    [
        sg.In(size = (10,1), enable_events=True, key = 'Nr'),
        sg.Text(size = (14, 1), font=('Helvetica', 9), justification='center', text_color = 'red', key='Nrtext')
    ],
    [
        sg.In(size =(10,1), enable_events=True, key = 'name')
    ]
]
button = sg.Button('Begin Test', bind_return_key = True)
buttoncol = [
    [button]
]
layout = [
    [sg.Column(column, justification = 'center'), sg.Column(inputcol)],
    [sg.Column(buttoncol, justification = 'center')]
]


# Window
window = sg.Window('Strain Intensity Test', layout, grab_anywhere = True, size = (350,300), font = default)

new = True
# Event Loop
while True:
    if new:
        pyautogui.getWindowsWithTitle('Strain Intensity Test')[0].activate()
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    validInput = True
    if event == 'Begin Test':
        digits = re.compile('\d+')
        keys = ['Ns','Nc','Nd','Nt','Nr']
        for k in keys:
          if digits.match(values[k]) is None:
            validInput = False
            window[k].Widget.configure(highlightcolor = 'red', highlightbackground ='red', highlightthickness=1)
            window[k+'text'].update('Must be a #')
        if validInput:
            for k in keys:
                window[k].Widget.configure(highlightcolor = bgcolor, highlightbackground = bgcolor)
                window[k+'text'].update('')
            Ns = int(values['Ns'])
            Nc = int(values['Nc'])
            Nd = int(values['Nd'])
            Nt = int(values['Nt'])
            Nr = int(values['Nr'])
            name = values['name']
            cycles = 0
            sensors = np.arange(1,Ns+1)
            prev = sensors[0]
            nums = []
            break
window.close()

# Start up MATLAB script  
pyautogui.getWindowsWithTitle('MATLAB R2022a - academic use')[0].activate()
pyautogui.write("strainintensity({}, {}, {}, {}, '{}')".format(Ns, Nc, Nd, Nr, name))
pyautogui.press('enter')

while True:
    time.sleep(3)
    # Start up UniVert
    titles = pyautogui.getAllTitles()
    r = re.compile('UniVert.*')
    uni = list(filter(r.match,titles))
    pyautogui.getWindowsWithTitle(uni[0])[0].activate()
    # Stop current test
    pyautogui.leftClick(x = 60, y = 96)
    time.sleep(2)
    # Creat new test
    pyautogui.hotkey('ctrl','n')
    pyautogui.press('enter')
    time.sleep(8)
    # Reset displacement
    pyautogui.leftClick(x = 186, y = 81)
    time.sleep(8)
    # Wait for input to start

    if cycles == 0:
        # Layout
        cycles = Nc
        if sensors.size > 0:
            sensornum = sensors[0]
        else:
            sensornum = prev
        text = 'Sensor #' + str(sensornum)
        button = sg.Button('Begin Test')
        redob = sg.Button('Redo')
        exitb = sg.Button('Finish')
        col = [
            [sg.Text('New Sensor #: ', size = (12,1), font = ('Helvetica', 15))]
        ]
        inputcol = [
            [
                sg.In(size = (10,1), key = 'newsensor', do_not_clear = False)
            ],
            [
                sg.Text(size = (14,1), font = ('Helvetica', 9), text_color = 'red', key='newsensortext')
            ]
        ]
        buttoncol = [
            [button,redob,exitb]
        ]
        layout = [
            [sg.Column(col, vertical_alignment = 'top',justification = 'center',key = 'col'),sg.Column(inputcol,key = 'inputcol')],
            [sg.Column(buttoncol, justification = 'center')]
        ]
        # Window  
        window = sg.Window('Input', layout, grab_anywhere = True, size = (250,150), font = default, finalize = True)
        window['newsensor'].bind('<Return>', '_enter')
        if sensornum == 1 or sensors.size <= 0:
            window['Redo'].update(visible = False)
        if sensors.size > 0:
            window['Finish'].update(visible = False)
        button.update(text)
        redob.update('Redo #' + str(prev))
        command = ''
        new = True
        # Event Loop
        while True:
            if new:
                new = False
                pyautogui.getWindowsWithTitle('Input')[0].activate()
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            validInput = True
            if event == 'Begin Test':
                prev = sensornum
                command = str(sensornum)
                sensors = sensors[sensors != sensornum]
                break
            if event == 'newsensor_enter':
                digits = re.compile('\d+')
                if digits.match(values['newsensor']) is None or int(values['newsensor']) > Ns or sensornum == 1 and int(values['newsensor']) == 1:
                    validInput = False
                    window['newsensor'].Widget.configure(highlightcolor = 'red', highlightbackground ='red', highlightthickness=1)
                    window['newsensortext'].update('Must be a # <' + str(Ns))
                if validInput:
                    button.update('Sensor #' + values['newsensor'])
                    sensornum = int(values['newsensor'])
                    window['newsensor'].Widget.configure(highlightcolor = bgcolor, highlightbackground = bgcolor)
                    window['newsensortext'].update('')
            if event == 'Redo':
                sensornum = prev
                command = 'r'
                break
            if event == 'Finish':
                command = 'q'
                break
        window.close()
        pyautogui.getWindowsWithTitle('MATLAB R2022a - academic use')[0].activate()
        pyautogui.write(command)
        pyautogui.press('enter')
        if command == 'q':
            break
        titles = pyautogui.getAllTitles()
        r = re.compile('UniVert.*')
        uni = list(filter(r.match,titles))
        pyautogui.getWindowsWithTitle(uni[0])[0].activate()
    
    time.sleep(1)
    cycles = cycles - 1
    # Start test  
    pyautogui.leftClick(x = 29, y = 96)
    pyautogui.getWindowsWithTitle('MATLAB R2022a - academic use')[0].activate()
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(21)
    
    Nt = Nt + 1
# Print test run numbers
print(nums)
