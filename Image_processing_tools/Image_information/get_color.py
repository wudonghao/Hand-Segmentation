from PIL import Image
image = Image.open("/home/wdh/PycharmProjects/Semantic Segmentation/Pytorch-UNet-master-milesial_self/test.jpg")
print(image,image.getcolors())

image = Image.open("/home/wdh/PycharmProjects/Semantic Segmentation/Pytorch-UNet-master-milesial_self/test_OUT.jpg")
print(image,image.getcolors())

image = Image.open("/home/wdh/PycharmProjects/Semantic Segmentation/Pytorch-UNet-master-milesial_self/truth1.png")
print(image)
