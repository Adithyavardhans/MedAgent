# ui/app.py

import os
from pathlib import Path

import gradio as gr
import pandas as pd

from src.inference import BiomedicalNERInference


BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "final_biobert_bc5cdr"
MEDQUAD_PATH = BASE_DIR / "medquad_ds"

ner = BiomedicalNERInference(
    model_path=str(MODEL_PATH),
    medquad_path=str(MEDQUAD_PATH) if MEDQUAD_PATH.exists() else None,
)


def analyze_with_medquad(file, text_input):
    # Read uploaded file or textbox input
    if file is not None:
        file_path = file if isinstance(file, str) else file.name
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    elif text_input and text_input.strip():
        text = text_input.strip()
    else:
        empty_df = pd.DataFrame(
            columns=["entity_text", "entity_type", "matched_question", "medquad_answer"]
        )
        grouped_df = pd.DataFrame(columns=["Category", "Entities"])
        return "No input provided.", empty_df, grouped_df, "No entities found."

    result = ner.analyze_text(text)

    detailed_df = result["detailed_df"]
    grouped_df = result["grouped_df"]
    summary = result["summary"]

    
    expected_cols = ["entity_text", "entity_type", "matched_question", "medquad_answer"]
    for col in expected_cols:
        if col not in detailed_df.columns:
            detailed_df[col] = ""

    detailed_df = detailed_df[expected_cols]

    return text, detailed_df, grouped_df, summary


demo = gr.Interface(
    fn=analyze_with_medquad,
    inputs=[
        gr.File(label="Upload Patient Report (.txt)", file_types=[".txt"]),
        gr.Textbox(
            label="Or Paste Medical Text Here",
            lines=12,
            placeholder="Paste a patient report or medical paragraph here..."
        )
    ],
    outputs=[
        gr.Textbox(label="Input Text", lines=12),
        gr.Dataframe(label="Extracted Entities + MedQuAD Explanations"),
        gr.Dataframe(label="Grouped Output"),
        gr.Textbox(label="Summary", lines=8)
    ],
    title="Biomedical NER + MedQuAD Explanation Assistant",
    description=(
        "Upload a patient report or paste medical text. "
        "The system extracts disease and chemical entities using BioBERT "
        "and retrieves related explanations from MedQuAD."
    )
)


if __name__ == "__main__":
    demo.launch()
