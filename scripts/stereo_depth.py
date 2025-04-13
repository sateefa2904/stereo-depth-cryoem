# stereo_depth.py
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Create results directory if not exists
os.makedirs("results", exist_ok=True)

# Load stereo pair images (make sure images/left.png and right.png exist)
imgL = cv2.imread("images/left.png", cv2.IMREAD_GRAYSCALE)
imgR = cv2.imread("images/right.png", cv2.IMREAD_GRAYSCALE)

if imgL is None or imgR is None:
    raise FileNotFoundError("Could not load the left and right images. Make sure they exist in the 'images' folder.")

# Initialize StereoBM matcher
stereo = cv2.StereoBM_create(numDisparities=64, blockSize=15)
disparity = stereo.compute(imgL, imgR)

# Normalize disparity for visualization
disp_normalized = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX)
disp_uint8 = np.uint8(disp_normalized)
cv2.imwrite("results/disparity_map.png", disp_uint8)

# Reproject to 3D (dummy Q matrix)
Q = np.float32([[1, 0, 0, -100],
                [0, -1, 0, 100],
                [0, 0, 0, -300],
                [0, 0, 1, 0]])
points_3D = cv2.reprojectImageTo3D(disparity, Q)

# 3D plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(np.arange(disp_uint8.shape[1]), np.arange(disp_uint8.shape[0]))
ax.plot_surface(X, Y, disp_uint8, cmap='viridis')
plt.title("Depth Map 3D Visualization")
plt.savefig("results/depth_map_3d.png")
plt.show()
