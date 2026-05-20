# 🛡️ AI Abusive Comment Detector

An interactive web application powered by Natural Language Processing (NLP) that detects toxic, abusive, and harmful comments in real-time. 

This project demonstrates the power of **Transfer Learning** by taking a massive, pre-trained language model (BERT) and fine-tuning it to perform a highly specific classification task.

## ✨ Features
* **Real-time Moderation:** Users can type any comment and instantly see if it is flagged as safe or abusive.
* **Context-Aware AI:** Unlike basic keyword filters, this model uses BERT's bidirectional architecture to understand the *context* and *intent* behind sentences.
* **Interactive Frontend:** A clean, user-friendly UI built entirely in Python using Streamlit.

## 🛠️ Technology Stack
* **Language:** Python
* **Model Architecture:** BERT (`bert-base-uncased`) via Hugging Face Transformers
* **Machine Learning Framework:** PyTorch
* **Data Manipulation:** Pandas
* **Web Framework:** Streamlit

## 🧠 How It Works
1. **Pre-processing:** Raw text is passed through a `BertTokenizer`, which converts human language into numerical token IDs and applies necessary padding/truncation.
2. **Transfer Learning:** The core model is a pre-trained BERT transformer. A specialized classification head was added to the top of this model and fine-tuned on a labeled dataset of social media comments.
3. **Inference:** When a user submits text, the model calculates the logits (mathematical probabilities) and outputs a binary classification: `0` (Clean) or `1` (Abusive).

## 🚀 How to Run Locally

If you want to run this project on your own machine, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/chau16/Abusive-Comment-Detector.git](https://github.com/chau16/Abusive-Comment-Detector.git)
cd Abusive-Comment-Detector# Abusive-Comment-Detector
Detecting toxic text using machine learning. A custom-trained BERT model wrapped in an interactive Streamlit frontend. #nlp #machine-learning #bert #pytorch #streamlit #python #transformers
