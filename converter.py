from wand.image import Image
import os

SourceFolder="/"
TargetFolder="/

for file in os.listdir(SourceFolder):
    if 'HEIC' in file:
        SourceFile=SourceFolder + "/" + file
        TargetFile=TargetFolder + "/" + file.replace(".HEIC",".jpg")

        img=Image(filename=SourceFile)
        img.format='jpg'
        img.save(filename=TargetFile)
        img.close()
print ('finished')
