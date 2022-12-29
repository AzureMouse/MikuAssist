"""
File:			client.py
Project:		MikuLive
Date			12/28/22
Author:			AzureMouse
Description:
"""
import pygame
import sys
from window import Window
# Main entry opoint of the program
def main():
	instance = Window()
	pygame.init() # -> Create an instance of pygame
	screen = pygame.display.set_mode((instance.get_width(), instance.get_height()))

	is_running = True

	while(is_running):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(instance.get_color())
		pygame.display.flip()

main()