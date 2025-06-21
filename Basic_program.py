import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_image(title, img, cmap=None):
    plt.figure(figsize=(10, 5))
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.axis('off')
    plt.show()


img = cv2.imread("C:/Users/gokul/Downloads/kitten.png")
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
show_image("original image", rgb_image)
