"""
File:			client.py
Project:		MikuLive
Date			12/28/22
Author:			AzureMouse
Description:
"""
import pygame
import sys
import cv2 # -> OpenCV
from window import Window
from video import Video

# Main entry point of the program
def main():

	# Instances
	window_instance = Window()
	video_instance = Video();

	pygame.init() # -> Create an instance of pygame
	screen = pygame.display.set_mode((window_instance.get_width(), window_instance.get_height()))
	video = cv2.VideoCapture(video_instance.get_video())

	is_running = True 

	while(is_running):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			while(video.isOpened()):

				ret, frame = video.read()
				if(ret):
					cv2.imshow('Frame', frame)

					if(cv2.waitKey(100) & 0xFF == ord('q')):
						break


				else:
					 video.set(cv2.CAP_PROP_POS_FRAMES, 0)
					 continue

		video.release()	
		cv2.destroyAllWindows()	

		screen.fill(window_instance.get_color())
		pygame.display.flip()

main()