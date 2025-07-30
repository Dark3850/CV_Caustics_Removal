# 🌊 CV Caustics Removal

**Computer Vision Corrections Enhance UAV-Based Retrievals in Shallow Waters**

<img src="media/demo.gif" alt="Demo" width="800"/>

---

## 🧭 Overview

Traditional methods for shallow water (<5 m) mapping are expensive and spatially constrained due to the complexity of sensor deployment in remote coastal zones. These limitations hinder wide-scale monitoring of ecologically critical near-shore benthic habitats.

This project leverages **Unmanned Aerial Vehicles (UAVs)** to collect high-resolution video data and introduces a novel processing pipeline to remove **optical distortions** such as:
- 💡 Light **refraction**
- 🌊 **Caustics**
- ✨ **Sun glint**

---

## 🔍 Methodology

In our study, we process Full-HD 60 FPS UAV videos captured at altitudes ranging from **10 m to 120 m**. Our approach includes:

- 🎞️ **Frame Extraction**
- 🧮 **Image Averaging (Median Filtering)**
- 🎨 **Color Transferring Correction**

---

## 📊 Key Results

In the final enhancement, we were able to achieve not only the restoration of the geometries, but also a color enhancement to better discriminate the underwater scenary.

<p float="left">
  <img src="media/input_frame.png" width="250"/>
  <img src="media/median_result.png" width="250"/>
  <img src="media/final_output.png" width="250"/>
</p>

---

## 🚀 Usage

### 🔧 Installation

Clone the repository and install required packages:

```bash
git clone https://github.com/Dark3850/CV_Caustics_Removal.git
pip install -r requirements.txt 
```

The Python version used in our work is `python==3.9.1`

### ▶️ Run the Pipeline

1. To download the sample video, use this [Drive link](https://drive.google.com/drive/folders/1fm17AQia0bVttX4vSvrwrepVpf3g033v?usp=sharing).  
2. Place the video file in the `Caustics_Removal` folder.  
3. Then simply run the `CV_Caustics_Removal.jpynb` notebook.

On a general note, you will find the ground truth image to perform the final enhancement correction in the `Caustics_Removal/5_Target` folder. This image was the one 
used in our study.

<img src="Caustics_Removal/5_Target/GT.JPG" width="800"/>

### ▶️ Run the Pipeline on your data

1. Be sure to put all your UAV videos in the `Caustics_Removal` folder.
2. Put your ground truth image in the `Caustics_Removal/5_Target` fodler. For more details on the GT iamge selection, look at our paper.
3. Run the `CV_Caustics_Removal.jpynb` notebook. The folder structure is already given in the repository.

## 📖 Cite Us

If you use this repository or the methods described herein in your work, please cite it as follows.
[Link](https://ieeexplore.ieee.org/abstract/document/11075526) to the article.
**BibTeX**
```bibtex
@ARTICLE{11075526,
  author={Scilla, Dario and Lopez, Omar A. and Nieuwenhuis, Brian Owain and Johansen, Kasper and Elías-Lara, Mariana and Angulo, Victor and Rodríguez, Jorge L. and Jones, Burton H. and McCabe, Matthew F.},
  journal={IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing}, 
  title={Computer Vision Corrections Enhance UAV-Based Retrievals in Shallow Waters}, 
  year={2025},
  volume={18},
  number={},
  pages={18134-18149},
  keywords={Image color analysis;Autonomous aerial vehicles;Optical distortion;Sun;Marine vegetation;Distortion;Videos;Shape;Water conservation;Sea measurements;Caustics;color transferring;computer vision;refraction;shallow waters;unmanned aerial vehicle (UAV)},
  doi={10.1109/JSTARS.2025.3587478}}