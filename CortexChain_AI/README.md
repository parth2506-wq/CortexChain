# 🧠 Generative AI Supply Chain Risk Prediction System

## 📌 Overview
This project is a **Generative AI–powered supply chain decision support system** that predicts future risks such as **stock-outs and demand spikes** and explains them in **natural language with actionable recommendations**.

The system combines **time-series forecasting (Machine Learning)** with **Generative AI reasoning** to help businesses move from **reactive monitoring** to **proactive decision-making**.

---

## 🎯 Problem Statement
Traditional supply chain systems detect problems **after losses occur**.  
While forecasting models predict demand, they do not explain:
- Why a risk exists
- What action should be taken
- When to act

### Solution
This project:
- Predicts future demand
- Detects upcoming supply chain risks
- Uses Generative AI to explain risks and suggest actions in plain English

---

## 🚀 Key Features
- 📈 Demand forecasting using time-series models (ARIMA / LSTM)
- 🚨 Automatic detection of stock-out and demand spike risks
- ✨ Generative AI explanations and recommendations
- 🖥️ Interactive dashboard using Streamlit
- 💬 Ask-the-AI interface for business questions

---

## 📊 Dataset
- **Source:** Kaggle – Store Item Demand Forecasting Dataset
- **Type:** Retail time-series sales data

### Dataset Enhancements
To simulate real-world supply chain behavior:
- Synthetic inventory levels are generated
- Supplier delay signals are added

### Final Dataset Schema
date, product_id, sales, inventory_level, supplier_delay

---

## 🧠 System Workflow
1. Load historical sales data
2. Forecast future demand
3. Detect supply chain risks
4. Generate AI explanations and recommendations
5. Display insights via interactive dashboard

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Data & Machine Learning
- Pandas
- NumPy
- Scikit-learn
- Statsmodels (ARIMA)

### Generative AI
- Large Language Model (LLM)
- Prompt-based reasoning for explanations

### Frontend
- Streamlit

---

## 📂 Project Structure

genai_supplychain_ai/
│
├── data/ # Raw & processed datasets
├── notebooks/ # Data exploration & experiments
├── src/ # ML models & Generative AI logic
├── dashboard/ # Streamlit application
├── outputs/ # Predictions & AI insights
├── config/ # Configuration files
└── demo/ # Hackathon presentation

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository
git clone <repository-url>
cd genai_supplychain_ai

### Step 2: Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

### Step 3: Install Dependencies
pip install -r requirements.txt

---

## ▶️ Running the Application

Launch the Streamlit Dashboard
streamlit run dashboard/streamlit_app.py

Open in browser:
http://localhost:8501

---

## 💡 Example Output

- ⚠️ Stock-out risk detected in next 5 days
- 📊 Demand forecast visualization
- ✨ AI-generated explanation:
“Demand for Product A is rising while inventory remains low. A stock-out is likely within 4–5 days. Recommended action: increase reorder quantity or shift inventory from nearby locations.”

## 🧑‍⚖️ Hackathon Value Proposition

- Combines Machine Learning + Generative AI
- Explainable and decision-focused AI
- Strong real-world business relevance
- Easy to demonstrate and evaluate

## 🔮 Future Enhancements

- Real-time data ingestion
- Multi-product optimization
- Automated reorder policy recommendations
- ERP system integration

## 👥 Team

Project developed for hackathon demonstration
Team : CortexChain

## 🏁 Conclusion
This project demonstrates how Generative AI can transform predictions into meaningful business decisions, enabling organizations to act before problems occur rather than reacting afterward.
