# 🌊 CV Caustics Removal

**Shallow Water Distortion Correction Using UAV Imagery and Color Transfer Techniques**

<img src="media/demo.gif" alt="Demo" width="700"/>

---

## 🧭 Overview

Traditional methods for shallow water (<5 m) mapping are expensive and spatially constrained due to the complexity of sensor deployment in remote coastal zones. These limitations hinder wide-scale monitoring of ecologically critical near-shore benthic habitats.

This project leverages **Unmanned Aerial Vehicles (UAVs)** to collect high-resolution video data and introduces a novel processing pipeline to remove **optical distortions** such as:
- 💡 Light **refraction**
- 🌊 **Caustics**
- ✨ **Sun glint**

---

## 🔍 Methodology

We process Full-HD 60 FPS UAV videos captured at altitudes ranging from **10 m to 120 m**. Our approach includes:

- 🎞️ **Frame Extraction**
- 🧮 **Image Averaging (Median Filtering)**
- 🎨 **Color Transferring Correction**

<p float="left">
  <img src="media/input_frame.png" width="300"/>
  <img src="media/median_result.png" width="300"/>
  <img src="media/final_output.png" width="300"/>
</p>

---

## 📊 Key Results

- **>10% improvement** in frame correlation at low altitudes (<20 m)
- **<5% shape error** in restored geometries
- Best results achieved using **60 consecutive frames**
- Strong performance vs traditional methods on:
  - Refraction
  - Caustics
  - Sun glint

---

## 🚀 Usage

### 🔧 Installation

Clone the repository and install required packages:

```bash
git clone https://github.com/Dark3850/CV_Caustics_Removal.git
cd CV_Caustics_Removal
pip install -r requirements.txt
