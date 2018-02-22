import webbrowser
import time
count = 0
loop = 3
print "Program Started at: " + time.ctime()
while count < loop:
	time.sleep(60)
	webbrowser.open("https://www.youtube.com/watch?v=CM_7I4xUIns")
	count += 1