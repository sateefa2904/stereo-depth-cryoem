# Stereo Depth Estimation on Cryo-EM Slices

![Stereo Vision Banner](https://raw.githubusercontent.com/sateefa2904/stereo-depth-cryoem/main/results/disparity_map.png)

A compact yet powerful stereo vision pipeline built around 3D biological data. This project demonstrates depth map generation and 3D surface visualization using stereo pairs extracted from a synthetic Cryo-Electron Microscopy (Cryo-EM) volume.

> 🧠 This is a general idea of the stereo algorithm I'm implementing in my research. Due to confidentiality, I cannot share real UTSW data or code directly. The project is part of an ongoing study on protein structural modeling in Cryo-EM reconstructions.

---

## 🧠 Project Overview

This repository walks through:

- Loading a `.mat`-based synthetic Cryo-EM 3D volume mimicking amyloid fibril structures
- Extracting two axial slices as a stereo pair (z=44 and z=46)
- Normalizing and saving the stereo images
- Computing disparity using OpenCV's `StereoBM`
- Visualizing the resulting depth map in 3D using matplotlib
- Exporting animated disparity results

---

## 📁 Folder Structure
```
StereoDepthProject/
├── images/
│   ├── left.png
│   └── right.png
├── results/
│   ├── disparity_map.png
│   ├── disparity_animation.gif
│   └── depth_map_3d.png
├── scripts/
│   └── stereo_depth.py
├── test_volume.mat
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/sateefa2904/stereo-depth-cryoem.git
cd stereo-depth-cryoem
```

### 2. (Optional) Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the Stereo Depth Script
```bash
python scripts/stereo_depth.py
```
Output images will be saved in the `results/` folder.

---

## 🖼 Example Outputs

### Stereo Input Pair
<p float="left">
  <img src="https://raw.githubusercontent.com/sateefa2904/stereo-depth-cryoem/main/images/left.png" width="200" />
  <img src="https://raw.githubusercontent.com/sateefa2904/stereo-depth-cryoem/main/images/right.png" width="200" />
</p>

### Depth Map Output
![Disparity Map](https://raw.githubusercontent.com/sateefa2904/stereo-depth-cryoem/main/results/disparity_map.png)

### 3D Visualization
![3D Plot](https://raw.githubusercontent.com/sateefa2904/stereo-depth-cryoem/main/results/depth_map_3d.png)

### Animated Disparity GIF
![Animated Disparity](https://raw.githubusercontent.com/sateefa2904/stereo-depth-cryoem/main/results/disparity_animation.gif)

---

## 🧬 Why Cryo-EM + Stereo Vision?

Cryo-EM (Cryogenic Electron Microscopy) is used to capture volumetric scans of biomolecules. By treating adjacent axial slices as left/right views, we can test stereo vision techniques on biomedical data.

This synthetic dataset is inspired by amyloid fibril stacking patterns. In real datasets, such disparity-driven depth estimation could complement segmentation tasks or be integrated into 3D structural prediction pipelines.

---

## 🔬 Research Connection
This stereo vision pipeline models a subset of methods I am applying in my current research at UTSW, where I work on neural approaches to Cryo-EM volume interpretation and alignment. Though the research involves real amyloid reconstructions, those datasets remain private. This public-facing version is a faithful conceptual demonstration designed for publication and portfolio purposes, and reflects potential research directions aligned with KAUST’s bioinformatics and computer vision interests.

---

## 🛠 Tech Stack
- Python 3.10+
- OpenCV
- NumPy
- Matplotlib

---

## 🌱 Future Ideas
- Swap StereoBM with `StereoSGBM` for smoother disparity
- Apply to real EMPIAR or RELION-aligned stacks
- Integrate with segmentation or refinement networks
- Auto-generate stereo pairs from 3D density maps
- Adapt pipeline for contrast transfer function (CTF)-aware pre-processing

---

## 👩🏽‍💻 Built By
**Soli Ateefa**  
Biomedical + AI Enthusiast · CS Honors @ UTA  
[LinkedIn](https://www.linkedin.com/in/sateefa2904/) • [Portfolio](https://sateefa2904.github.io)

---

## 🧪 License
This project is for educational and demo purposes. All Cryo-EM simulations used are synthetic and freely shareable.

