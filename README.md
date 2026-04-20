# MedAgent: Biomedical Entity Extraction and Explanation System

## Project Overview

MedAgent is an end-to-end biomedical Natural Language Processing (NLP) system designed to extract clinically relevant entities from unstructured patient reports.

The system identifies disease and chemical entities using a fine-tuned BioBERT model and enhances interpretability by retrieving explanations from the MedQuAD dataset.

It demonstrates a complete pipeline from raw text input to structured output and explanation, along with an interactive user interface.

---

## Key Features

- Biomedical Named Entity Recognition (NER) using BioBERT  
- Extraction of Disease and Chemical entities  
- MedQuAD-based explanation retrieval  
- Support for synthetic patient reports using Synthea  
- Interactive Gradio interface (file upload and text input)  
- End-to-end pipeline from input to interpretable output  

---

## Datasets Used

- BC5CDR: Training dataset for BioBERT NER  
- Synthea: Synthetic patient reports for testing  
- MedQuAD: Retrieval of explanations for extracted entities  

---

## Model Details

- Model: BioBERT (dmis-lab/biobert-base-cased-v1.2)  
- Task: Token classification for NER  
- Labels: Disease, Chemical  
- Training Dataset: BC5CDR  
- Epochs: 3  
- Learning Rate: 2e-5  

---

## Project Structure

```
MedAgent/
├── data/        # Synthea generated test reports
├── docs/        # IEEE report and architecture diagram
├── notebooks/   # Full Colab notebook (training + evaluation + UI)
├── results/     # Metrics, confusion matrix, UI screenshots
├── src/         # Inference pipeline (model loading and prediction)
├── ui/          # Gradio interface (app.py)
├── README.md
└── requirements.txt
```

---

## Results

The model achieves strong performance on the BC5CDR test dataset:

- Precision: 0.8416  
- Recall: 0.8919  
- F1 Score: 0.8660  
- Accuracy: 0.9665  

## Refinements

- Added explanation-level output using MedQuAD (`medquad_answer`)
- Refined Gradio UI with structured layout and clearer sections
- Introduced Analyze and Clear controls for better interaction
- Improved output presentation with grouped entities and summary
- Stabilized pipeline by loading the trained model from disk

## Sample Output

Example output from the system:

- Diseases: Prediabetes, Anemia, Obesity, Pain  
- Chemicals: Alcohol, Acetaminophen, Glucose  

Each entity is accompanied by:
- Matched MedQuAD question  
- Retrieved explanation (where available)  

Refer to `results/` for full UI screenshots.

### Observations

- High recall indicates effective entity detection  
- Slightly lower precision suggests minor false positives  
- Chemical entities are identified more consistently than disease entities  
- Most errors occur near entity boundaries  

---

## How to Run

### Option 1: Using Notebook

Open the notebook in the `notebooks/` folder and run all cells to train, evaluate, and test the model.

### Option 2: Running the UI

```bash
cd ui
python app.py
```

Then open the Gradio interface in your browser.

---

## System Workflow

- Input patient report (file or text)  
- Preprocessing and tokenization  
- BioBERT performs entity extraction  
- Entities are grouped into Disease and Chemical categories  
- MedQuAD retrieves explanations  
- Structured output is displayed via the interface  

---

## Limitations

- MedQuAD retrieval is keyword-based and not semantic  
- Model may produce false positives in entity detection  
- The system is not intended for clinical diagnosis or decision-making  

---

## Future Work

- Implement semantic retrieval for better explanation accuracy  
- Improve entity boundary detection  
- Enhance user interface visualization  
- Extend system toward biomedical question answering  

---

## Conclusion

MedAgent demonstrates a complete biomedical NLP pipeline that integrates entity extraction and explanation retrieval.

The system combines BioBERT and MedQuAD to provide both accurate predictions and interpretable outputs, forming a strong foundation for future biomedical AI applications.
