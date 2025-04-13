# visualize_cityscapes.py
import cv2
import matplotlib.pyplot as plt
import os

# Define paths to your dataset
image_path = 'data/train/images/sample_image.png'
depth_path = 'data/train/depths/sample_depth.png'

# Load images
image = cv2.imread(image_path)
depth = cv2.imread(depth_path, cv2.IMREAD_GRAYSCALE)

# Display them side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('RGB Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Ground Truth Depth Map')
plt.imshow(depth, cmap='plasma')
plt.axis('off')

plt.tight_layout()
plt.show()
