from PIL import Image
import os
import numpy as np

def change(dir):
    file_list = os.listdir(dir)
    print(file_list)
    for filename in file_list:
        path = ''
        path = dir+filename
        img = Image.open(path).convert("L")        
        table=[]
        for i in range(256):
            if i <100:
                table.append(0)
            else:
                table.append(1)

        out = img.point(table,"P")
        out.save(path)                   
        print("%s has been recolored!"%filename)

if __name__ == '__main__':
#   dir = input('please input the operate dir:')
   dir = "/home/wdh/PycharmProjects/Semantic Segmentation/Pytorch-UNet-master-milesial_self/ad/"
   change(dir)
