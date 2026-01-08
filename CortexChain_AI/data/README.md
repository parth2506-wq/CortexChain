# Dataset Documentation

## Overview

This folder contains all datasets used in the CortexChain_AI project.

The data is primarily used for:
- Training forecasting models
- Detecting supply chain risks
- Feeding Generative AI explanations

--- 

## Dataset Sources

### 1. Kaggle Store Item Demand Dataset
- Source: Kaggle – Store Item Demand Forecasting
- Type: Time-series sales data
- Features:
  - date → Date of sale
  - store → Store ID
  - item → Item ID
  - sales → Number of items sold
 
### 2. Synthetic / Enhanced Features
- To simulate realistic supply chain scenarios, the following were added:
   - inventory_level → Current inventory of the product
   - supplier_delay → Simulated supplier delays in days
   - demand_spike_flag → Indicates unusual sales spikes

---

## Folder Structure
- raw/ → Original, unprocessed dataset
   - Example: store_item_sales.csv
- processed/ → Cleaned and feature-engineered dataset ready for modeling
   - Example: final_dataset.csv

---

## Usage Guidelines
- Always keep raw data unchanged in raw/
- All preprocessing and feature engineering should output to processed/
- Use processed/ dataset for training ML models and generating insights

---

## Notes
- The data is time-series structured, suitable for ARIMA, LSTM, or other forecasting models
- Any missing or anomalous data is handled in preprocessing
- Generated features (inventory, supplier delays) are synthetic for demonstration purposes
