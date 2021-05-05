import glob
import shutil
import os	
from progress.bar import Bar

directory = "C:/Users/Mestik78/downloads/Mestik78/"
clips = glob.glob(directory + "*.mp4")


		

def processClip(clipFullName):
	clip = clipFullName.split("\\")[1]
	clipWords = clipFullName.split(" ")
	clipDateText = clipWords[len(clipWords)-2]

	class Date(object):
		Day = clipDateText[0:2]
		Month = clipDateText[2:4]
		Year = clipDateText[4:8]

	newPath = directory + "/Output/" + Date.Year + "/" + Date.Month + "/" + Date.Day + "/" + clip

	os.makedirs(os.path.dirname(newPath), exist_ok=True)
	shutil.copy(clipFullName, newPath)


with Bar('Ordering', fill='█', suffix='%(percent).1f%% | %(index)d/%(max)d | eta: %(eta)ds', max=len(clips)) as bar:
	for clip in clips:
		processClip(clip)
		bar.next()