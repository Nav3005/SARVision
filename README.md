# **Vision-Driven Architecture for Translating, Segmenting & Interpreting Radar-Based Satellite Imagery**

This repository presents a complete deep learning framework designed to **analyse, extract, and convert Synthetic Aperture Radar (SAR) imagery into human-understandable visual and textual outputs**.  
The system integrates three major components:

- **SAR-to-Optical Translation**  
- **Semantic Segmentation**  
- **Vision-Language Landscape Interpretation**

Together, these modules form a unified pipeline aimed at supporting geospatial intelligence, disaster response, environmental monitoring, and defense surveillance.

---

## **📌 Features**

### **1. SAR → Optical Image Translation**
- Uses **Pix2Pix / CycleGAN / Diffusion-based models**.
- Converts SAR backscatter into optical-like RGB images.
- Preserves spatial structure across terrain types.
- Evaluated using **SSIM**, **PSNR**, and perceptual similarity metrics.

### **2. Semantic Segmentation**
- Based on **Swin-UNet / DeepLabv3+** architectures.
- Performs pixel-level extraction of:
  - Roads  
  - Buildings  
  - Rivers  
  - Vegetation  
- Evaluated using **IoU**, **Dice Score**, and **Pixel Accuracy**.

### **3. Vision-Language Interpretation**
- Utilizes **LLaVA / BLIP / Custom VLMs**.
- Generates human-readable scene descriptions:
  - Terrain  
  - Landcover categories  
  - Structural patterns  
  - Environmental context  
- Supports caption generation on uploaded images.

---

## **📁 Project Structure**

```
├── data/
│   ├── SEN12MS/                 # SAR–RGB paired dataset
│   ├── MassRoads/               # Road segmentation dataset
│   └── CaptionDataset/          # Satellite captioning dataset
│
├── preprocessing/
│   ├── sar_rgb_preprocess.py
│   ├── segmentation_preprocess.py
│   └── caption_preprocess.py
│
├── models/
│   ├── pix2pix/
│   ├── swin_unet/
│   └── llava_captioning/
│
├── training/
│   ├── train_pix2pix.ipynb
│   ├── train_segmentation.ipynb
│   └── train_captioning.ipynb
│
├── inference/
│   ├── translate.py
│   ├── segment.py
│   └── generate_caption.py
│
├── app/
│   └── streamlit_app.py
│
└── README.md
```

---

## **📦 Datasets Used**

### **1. SEN1–SEN2 SAR–RGB Paired Dataset**
- SAR and optical image pairs for supervised translation.
- Covers multiple terrains: agricultural, forest, urban, desert, etc.

### **2. Massachusetts Road Segmentation Dataset**
- High-resolution aerial imagery with labeled road masks.
- Suitable for training road extraction pipelines.

### **3. Satellite Image Captioning Dataset**
- Images paired with natural-language captions.
- Enables training of the Vision-Language Interpretation module.

---

## **🧠 Model Architectures**

| Task | Model | Key Benefit |
|------|--------|--------------|
| SAR→Optical Translation | Pix2Pix, CycleGAN, Diffusion | Accurate multimodal translation |
| Semantic Segmentation | Swin-UNet, DeepLabv3+ | Global attention + fine-grained segmentation |
| Captioning | LLaVA, BLIP | Natural-language reasoning over geospatial imagery |

---

## **🧪 Evaluation Metrics**

### **Translation**
- **SSIM**  
- **PSNR**  
- **L1 Loss**  
- **Perceptual Loss**

### **Segmentation**
- **IoU**  
- **Dice Score**  
- **Precision, Recall**

### **Captioning**
- **BLEU**
- **ROUGE-L**
- **CIDEr**
- **METEOR**

---

## **🚀 How to Run**

### **1. Install Environment**

```bash
conda create -n radar_env python=3.10
conda activate radar_env
pip install -r requirements.txt
```

### **2. Launch Streamlit App**
```bash
streamlit run app/streamlit_app.py
```

This interface allows users to:
	•	Upload SAR images
	•	Convert them to optical-like images
	•	Generate segmentation masks
	•	Produce natural-language scene descriptions

💡 Applications
	•	Defense & Surveillance
	•	Night-time & all-weather imaging
	•	Monitoring sensitive border regions
	•	Disaster Management
	•	Flood mapping
	•	Damage assessment
	•	Environmental Monitoring
	•	Land-use change
	•	Deforestation
	•	Urban Infrastructure Analysis
	•	Road extraction
	•	Settlement mapping
