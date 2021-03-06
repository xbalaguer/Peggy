

#plot histograms
#calculates grayscale/color and 2d histograms
#see https://lmcaraig.com/image-histograms-histograms-equalization-and-histograms-comparison/


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
import cv2
import numpy as np
from matplotlib import ticker

#Load paaramters
image = mpimg.imread("/home/pi/Desktop/testimage6.jpg")




def draw_image_histogram(image, channels, color='k'):
    hist = cv2.calcHist([image], channels, None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])


def show_grayscale_histogram(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    draw_image_histogram(grayscale_image, [0])
    plt.show()

def show_color_histogram(image):
    for i, col in enumerate(['b', 'g', 'r']):
        draw_image_histogram(image, [i], color=col)
    plt.show()

    


def show_image_histogram_2d(image, bins=32, tick_spacing=5):
    fig, axes = plt.subplots(1, 3, figsize=(12, 5))
    channels_mapping = {0: 'B', 1: 'G', 2: 'R'}
    for i, channels in enumerate([[0, 1], [0, 2], [1, 2]]):
        hist = cv2.calcHist(
            [image], channels, None, [bins] * 2, [0, 256] * 2)

        channel_x = channels_mapping[channels[0]]
        channel_y = channels_mapping[channels[1]]

        ax = axes[i]
        ax.set_xlim([0, bins - 1])
        ax.set_ylim([0, bins - 1])

        ax.set_xlabel('Channel {channel_x}')
        ax.set_ylabel('Channel {channel_y}')
        ax.set_title('2D Color Histogram for {channel_x} and {channel_y}')

        ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

        im = ax.imshow(hist)

    fig.colorbar(im, ax=axes.ravel().tolist(), orientation='orizontal')
    fig.suptitle('2D Color Histograms with {bins} bins', fontsize=16)
    plt.show()

#call functions 

show_image_histogram_2d(image,32,5)

show_color_histogram(image)

show_grayscale_histogram(image)
