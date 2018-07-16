from PIL import Image
import os
import numpy as np
filelist = []  
path = "/home/wdh/DataSets/hand-segmentation/From Cai/Resize/Masks/"
files = os.listdir(path)
for f in files:  
    if(os.path.isfile(path + '/' + f)):
        if (os.path.splitext(f)[1] == ".bmp"):
            filelist.append(f)
        if (os.path.splitext(f)[1] == ".jpg"):
            filelist.append(f)
        if (os.path.splitext(f)[1] == ".png"):
            filelist.append(f)
for infile in filelist:
    print(infile)
    outfile = os.path.splitext(infile)[0] + ".gif"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
            print("Covert to GIF successfully!")
        except IOError:
            print("This format can not support!", infile)
