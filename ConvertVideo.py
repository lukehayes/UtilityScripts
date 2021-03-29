# -------------------------------------------------------------
# This script uses the FFMpeg library to bulk convert .MOV
# files into .MP4 versions.
# -------------------------------------------------------------
from glob import glob
import os

# File/Path Variables
currentDir = os.getcwd()
outputDir = "Converted"
fileExt = ".mp4"
path = currentDir + "/../" + outputDir


# File Extension Regex
files = glob('*.MOV')
files.extend(glob('*.mov'))


# Make An Output Directory
try:
    os.mkdir(outputDir)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)


# Convert Each File
for file in files:
    split = os.path.splitext(file)
    name = split[0]
    ext = split[1]

    print("Converting " + name + " " + ext )
    os.system("ffmpeg -i " + file + " -qscale 0 " + outputDir + "/" + name + ".mp4")
