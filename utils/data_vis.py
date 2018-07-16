import matplotlib.pyplot as plt


def plot_img_mask(img, mask):
    fig = plt.figure()

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_title('Input image')
    ax1.imshow(img)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_title('Mask image')
    ax2.imshow(mask)

    plt.show()
