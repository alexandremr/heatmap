import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

img = cv2.imread('img.jpg')
df = pd.read_csv('points.csv')

mask = np.zeros(img.shape[:2], dtype=np.uint8)
for _, row in df.iterrows():
    cv2.circle(mask, (row['x'], row['y']), radius=15, color=(255, 255, 255), thickness=-1)

mask = cv2.GaussianBlur(mask, (101, 101), 11)
heatmap_img = cv2.applyColorMap(mask, cv2.COLORMAP_JET)
superimposed_img = cv2.addWeighted(heatmap_img, 0.5, img, 0.5, 0)

cv2.imshow('mask', mask)
cv2.imshow('heatmap_img', heatmap_img)
cv2.imshow('superimposed_img', superimposed_img)
cv2.waitKey(0)