# 3DGS Product Preprocessing Pipeline

A modular preprocessing pipeline for generating high-quality datasets for **3D Gaussian Splatting (3DGS)** reconstruction of consumer products. This project is part of my undergraduate final year research titled:

> **Enhancing Online Shopping Experience Through 3D Gaussian Splatting-Based Interactive Product Visualization for E-Commerce Platforms**

---

## Project Overview

The goal of this project is to design and implement a complete preprocessing pipeline that prepares multi-view product images for 3D Gaussian Splatting reconstruction.

The pipeline focuses on improving reconstruction quality through automated image quality assessment, cleaning, segmentation, and dataset preparation before camera pose estimation using COLMAP.

---

## Objectives

- Extract frames from captured product videos
- Validate image quality and integrity
- Detect and remove blurry images
- Detect and remove duplicate images
- Analyze exposure consistency
- Generate segmentation masks using SAM 2
- Produce dataset quality reports
- Prepare cleaned datasets for COLMAP and 3DGS

---

## Planned Pipeline

```text
Video Capture
      │
      ▼
Frame Extraction
      │
      ▼
Image Validation
      │
      ▼
Blur Detection
      │
      ▼
Duplicate Detection
      │
      ▼
Exposure Analysis
      │
      ▼
SAM 2 Segmentation
      │
      ▼
Quality Report
      │
      ▼
COLMAP
      │
      ▼
3D Gaussian Splatting
```

---

## Project Structure

```text
3dgs-product-preprocessing-pipeline/

├── configs/
├── data/
├── docs/
├── notebooks/
├── reports/
├── scripts/
├── src/
│   ├── extraction/
│   ├── validation/
│   ├── cleaning/
│   ├── segmentation/
│   ├── reporting/
│   └── utils/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Technologies

- Python 3.x
- OpenCV
- NumPy
- Pandas
- Pillow
- ImageHash
- Matplotlib
- FFmpeg
- SAM 2
- COLMAP
- 3D Gaussian Splatting

---

## Development Roadmap

### Phase 1

- [ ] Project setup
- [ ] Frame extraction
- [ ] Image validation

### Phase 2

- [ ] Blur detection
- [ ] Duplicate detection
- [ ] Exposure analysis

### Phase 3

- [ ] SAM 2 segmentation
- [ ] Dataset quality report
- [ ] Pipeline integration

### Phase 4

- [ ] COLMAP preprocessing
- [ ] 3DGS reconstruction
- [ ] Evaluation

---

## Dataset

The pipeline is designed to support:

- Custom captured product videos
- Public datasets (e.g., CO3D)
- Future support for additional object datasets

---

## Current Status

🟢 Project initialization completed

- Repository created
- Virtual environment configured
- Folder structure created
- Development environment ready

Next milestone:

> Implement the **Frame Extraction** module.

---

## License

This repository is developed for academic and research purposes as part of an undergraduate final year project.

---

## Author

**H.P.G. Themiya Dulshan**

Computer Science Undergraduate

University of Sri Jayewardenepura

## Pipeline Progress

| Module              | Status         |
| ------------------- | -------------- |
| Frame Extraction    | ⏳ In Progress |
| Image Validation    | ⬜ Not Started |
| Blur Detection      | ⬜ Not Started |
| Duplicate Detection | ⬜ Not Started |
| Exposure Analysis   | ⬜ Not Started |
| SAM 2 Segmentation  | ⬜ Not Started |
| Quality Report      | ⬜ Not Started |
| COLMAP Integration  | ⬜ Not Started |
| 3DGS Reconstruction | ⬜ Not Started |
