# -*- coding: utf-8 -*-
# By Mohamed Marzouk
# facebook.com/MohamedMarzouk23
import os
def renameFiles():
	files_list = os.listdir(r"D:\Programming\My Projects\UdacityFullStakePython\Secret_Message\prank")
	os.chdir("D:\Programming\My Projects\UdacityFullStakePython\Secret_Message\prank")
	for file in files_list:
		os.rename(file, file.translate(None, "0123456789"))
renameFiles()