 Brain Tumor Segmentation using Deep Learning


This project focuses on automatic brain tumor segmentation from MRI scans using deep learning. The model performs pixel-level classification to identify tumor regions in brain MRI images.

A CNN-based segmentation model (U-Net / ResUNet style) is used for training on MRI images and corresponding masks.


 Project Objectives
- Detect brain tumor regions from MRI scans
- Perform pixel-wise segmentation
- Train a deep learning model for medical image analysis
- Visualize predictions vs ground truth masks


---

## 🧠 Model Architecture
A U-Net based architecture is used:

- Encoder extracts features from MRI images  
- Decoder reconstructs segmentation masks  
- Skip connections preserve spatial details  

Optional: ResUNet (ResNet encoder + U-Net decoder) can also be used.

---

##  Dataset
- MRI brain scans with corresponding segmentation masks  
- Binary labels:
  - 0 → Background  
  - 1 → Tumor  

### Preprocessing:
- Resize images (e.g., 256×256)  
- Normalize pixel values (0–1)  
- Convert masks to binary format  
- Data augmentation (rotation, flipping, zooming)






