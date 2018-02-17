import numpy as np
import cv2
from grabscreen import grab_screen
from directkeys import PressKey, ReleaseKey, W, A, S, D
import win32api as wapi
import time
import os


keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys
 
def keys_to_output(keys):
	output = [0, 0, 0]

	if 'A' in keys:
		output[0] = 1

	elif 'D' in keys:
		output[2] = 1

	else:
		output[1] = 1 

	return output

file_name = 'Training_data.npy'
if os.path.isfile(file_name):
	prnt('File exists, loading previous data')
	Training_data = list(np.load(file_name))
else:
	print('file doesnot exists')
	Training_data = []

def main():
	for i in list(range(14))[::-1]:
	    print(i+1)
	    time.sleep(1)

	while True:
	    screen =  grab_screen(region=(0,40,800,600))
	    screen =cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
	    screen = cv2.resize(screen, (240,180))
	    keys = key_check()
	    output = keys_to_output(keys)
	    Training_data.append([screen,output])

	    if len(Training_data) % 500 == 0:
	    	print(len(Training_data))
	    	np.save(file_name, Training_data)

main()
