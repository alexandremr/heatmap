import pandas as pd
import cv2
import numpy as np

img = cv2.imread('img.jpg')
df = pd.read_csv('points.csv')

mask_total = np.zeros(img.shape[:2], dtype=np.float32)
mask = np.zeros(img.shape[:2], dtype=np.uint8)
for _, row in df.iterrows():
    local_mask = mask.copy()
    for radius, intensity in zip([30, 25, 20, 15, 10, 5], [1, 2, 3, 4, 5, 6]):
        cv2.circle(local_mask, (row['x'], row['y']), radius=radius, color=intensity, thickness=-1)
    mask_total += local_mask

mask_total = cv2.GaussianBlur(mask_total, (71, 71), 7)
mask_total = mask_total / mask_total.max() * 255
mask_total = mask_total.astype(np.uint8)

heatmap_img = cv2.applyColorMap(mask_total, cv2.COLORMAP_JET)

alpha = mask_total.astype(float) / 255.0
# Apply weighted blending using array operations
img = (alpha[..., None] * heatmap_img) + ((1 - alpha[..., None]) * img)
img = img.astype(np.uint8)

cv2.imshow('mask', mask_total)
cv2.imshow('heatmap_img', heatmap_img)
cv2.imshow('super_imposed_img', img)
cv2.waitKey(0)
