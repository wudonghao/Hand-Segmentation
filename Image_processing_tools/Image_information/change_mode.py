from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
path = "/home/wdh/PycharmProjects/Semantic Segmentation/Pytorch-UNet-master-milesial_self/output.jpg"
img = Image.open(path)
img1=img.convert("P")
ax1.imshow(img1)
plt.show()
