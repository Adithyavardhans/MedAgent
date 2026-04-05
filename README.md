# MedAgent Lite: Medical Report Understanding System

## Overview
This project focuses on making medical information easier to understand. Medical reports are often written in complex clinical language, which can be difficult for patients to interpret. This project converts structured medical data into simple, patient-friendly reports using basic data processing and machine learning techniques.

## Features
- Load datasets (PubMed, MedQuAD, Synthea)
- Generate synthetic medical reports from structured patient data
- Convert medical information into readable text
- Provide simple explanations for medical terms

## Project Structure
```
MedAgent/
├── data/          # Placeholder for datasets (not stored due to size)
├── notebooks/     # Jupyter notebooks
│   └── setup.ipynb
├── src/           # Helper scripts (future work)
├── ui/            # Interface (planned)
├── results/       # Outputs and visualizations
├── docs/          # Diagrams and documentation
├── requirements.txt
├── README.md
```

## Setup
```bash
pip install -r requirements.txt
```

## Run
Open the notebook:
```
notebooks/setup.ipynb
```

## Dataset
- **Synthea** – Synthetic patient records (conditions, medications, observations)
- **PubMed 200k RCT** – Medical research text dataset
- **MedQuAD** – Medical question-answer dataset

Note:  
Datasets are not stored in this repository due to size constraints.  
They are either generated (Synthea) or loaded dynamically in the notebook.
