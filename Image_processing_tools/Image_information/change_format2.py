from PIL import  Image
import numpy as np
#  load a color image 
im  =  Image.open("0000000118rahul_turkey.png")

#  convert to grey level image 
Lim  =  im.convert("L")
Lim.save("1.png")

#  setup a converting table with constant threshold 
threshold  =   80 
table  =  []
for  i  in  range( 256 ):
    if  i  <  threshold:
        table.append(0)
    else:
        table.append( 1 )

#  convert to binary image by the table 
bim  =  Lim.point(table, "P")

bim.save("2.png") 
im2 = np.array(Image.open("2.png"))
print("1")
