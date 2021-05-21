# --------------------------------------------------------------------
# Pyxel Art (Pixel art through Python)
# Converts an image to pixel art using a palette from palette_list.py
# Palettes can be added to the palette list using hex_2_rgb_palette.py
# Creator: RM13-Pixel
# --------------------------------------------------------------------
import cv2
import palette_list
from math import *
import os
from PIL import Image

# variables
path = "GO.jpg"  # the image to be converted
palette = palette_list.pixel_ink_2 # the palette(from palette_list.py)
minsize = 50  # the minimum size of the new square image (length of a side in pixels)

# jpg to large png
image = cv2.imread(path)
cv2.imwrite("gray.png", image)
path = "gray.png"
image = cv2.imread(path)
height, width = image.shape[0], image.shape[1]
while height > minsize * 2:
    height, width = height // 2, width // 2

# large png to small png
img_resize = cv2.resize(image, (height, width))
cv2.imwrite("final.png", img_resize)
og = cv2.imread("final.png", 1)
# cv2.imshow("Original",og)

# small png to grayscale
gray = cv2.cvtColor(og, cv2.COLOR_RGBA2GRAY)
cv2.imwrite("Gray.png", gray)

# small png in Image type
img = Image.open("final.png")

# grayscale values
colors = []
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        if gray[i][j] not in colors:
            colors.append(gray[i][j])
colors.sort()

# replace small png colors with palette based on greyscale values
num = len(colors) / len(palette)
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        idx = colors.index(gray[i][j])
        idx_new = ceil(idx / num) - 1
        if idx_new == -1:
            idx_new = 0
        # print(palette[idx_new])
        img.putpixel((j, i), palette[idx_new])

# save and display image
img.save("final.png")
recolored = cv2.imread("final.png")
# cv2.imshow("final", recolored)

# delete excess files
os.remove("gray.png")

