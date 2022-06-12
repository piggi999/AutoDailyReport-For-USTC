import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time

# 行程
bbox = [138, 237, 294, 258, 16]  # 行程码时间位置(:4)以及字体大小(-1)
color = (120, 120, 120)
img = cv2.imread("xcm.jpg")
shp = (bbox[2] - bbox[0], bbox[3] - bbox[1])
im = Image.new("RGB", (shp[0] + 20, shp[1]), (254, 254, 254))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype("arial.ttf", bbox[4])

dr.text((0, 0), time.strftime("%Y.%m.%d %H:%M:%S",
                              time.localtime(time.time()+8*3600-30)), color, font)
img[bbox[1]:bbox[3], bbox[0]:bbox[2], :] = cv2.resize(np.array(im), shp)
cv2.imwrite("xcm.jpg", img)
