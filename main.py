import os
import shutil
os.chdir('D:/Downloads')

files = os.listdir()

for file in files:
    if not os.path.exists(file[-3:]):
        os.mkdir(str(file[-3:]))
        shutil.move(file, file[-3:])
    elif os.path.exists(file[-3:]):
        shutil.move(file, file[-3:])