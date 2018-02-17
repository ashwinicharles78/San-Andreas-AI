import numpy as np 
from PIL import ImageGrab
import cv2
import pyautogui
from directkeys import PressKey, W, A, S, D

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(image):
	processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
	return processed_image

def main():

	while (True):
		#PressKey(W)
		printscreen_PIL = np.array(ImageGrab.grab(bbox=(0,40,640,480))) 
		new_screen = process_img(printscreen_PIL)

		cv2.imshow('window', new_screen)
		if cv2.waitKey(25) & 0xff == ord('q'):
			cv2.destroyAllWindows()
			break 
