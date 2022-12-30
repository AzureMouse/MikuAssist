"""
File:			video.py
Project:		MikuAssist
Date:			12/30/22
Author:			AzureMouse
Description:	
Handles the video/gif asspect to MikuAssist
"""
class Video:
	def __init__(self, video_target="miku.mp4"):
		self.video_target = video_target

	def get_video(self):
		return self.video_target

