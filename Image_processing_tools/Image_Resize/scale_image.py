# coding = utf-8  
from PIL import Image  

def  convert(width,height):
    im = Image.open("/home/wdh/PycharmProjects/Image_processing_tools/Image_Resize/img_00124.jpg")
#    (x, y)= im.size
#    x_s = int(width)
#    y_s = int(y * x_s / x)
    out = im.resize((width, height), Image.ANTIALIAS)
    out.save("/home/wdh/PycharmProjects/Image_processing_tools/Image_Resize/img_00124.jpg_out.jpg")
if __name__ == '__main__':
    convert(1918,1280)
