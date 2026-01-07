import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="GenAI Supply Chain Dashboard",
    layout="wide"
)

st.title("📦 Generative AI – Supply Chain Risk Dashboard")
st.markdown("Predict future risks and get AI-driven explanations")

# ------------------------------
# Load Data
# ------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/final_dataset.csv")

try:
    df = load_data()
except:
    st.error("Processed dataset not found. Please add data to data/processed/")
    st.stop()

# ------------------------------
# Sidebar Controls
# ------------------------------
st.sidebar.header("Controls")

product_list = df["product_id"].unique()
selected_product = st.sidebar.selectbox(
    "Select Product",
    product_list
)

# ------------------------------
# Load Data
# ------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/final_dataset.csv")

df = load_data()

if df is None or df.empty:
    st.error("Dataset is empty or not found.")
    st.stop()

product_df = df[df["product_id"] == selected_product]

# ------------------------------
# KPI Section
# ------------------------------
latest_row = product_df.iloc[-1]

col1, col2, col3 = st.columns(3)

col1.metric(
    "📊 Latest Sales",
    int(latest_row["sales"])
)

col2.metric(
    "📦 Inventory Level",
    int(latest_row["inventory_level"])
)

risk_status = (
    "⚠️ Stock-out Risk"
    if latest_row["predicted_demand"] > latest_row["inventory_level"]
    else "✅ Safe"
)

col3.metric(
    "🚨 Risk Status",
    risk_status
)

# ------------------------------
# Sales & Forecast Chart
# ------------------------------
st.subheader("📈 Sales & Demand Forecast")

fig, ax = plt.subplots()
ax.plot(product_df["date"], product_df["sales"], label="Actual Sales")
ax.plot(product_df["date"], product_df["predicted_demand"], label="Forecast")
ax.set_xlabel("Date")
ax.set_ylabel("Units")
ax.legend()

st.pyplot(fig)

# ------------------------------
# Risk Explanation (GenAI)
# ------------------------------
st.subheader("🤖 AI Risk Explanation")

def generate_ai_explanation(row):
    if row["predicted_demand"] > row["inventory_level"]:
        return (
            f"Product **{selected_product}** is likely to face a stock-out soon. "
            f"Predicted demand ({int(row['predicted_demand'])}) is higher than "
            f"current inventory ({int(row['inventory_level'])}). "
            "Recommended action: Increase reorder quantity or shift stock from nearby locations."
        )
    else:
        return (
            f"Product **{selected_product}** is currently safe. "
            "Inventory levels are sufficient to meet forecasted demand."
        )

ai_text = generate_ai_explanation(latest_row)

st.info(ai_text)

# ------------------------------
# Ask AI (Bonus Feature)
# ------------------------------
st.subheader("💬 Ask the AI")

user_question = st.text_input(
    "Ask something like: Why is this product at risk?"
)

if user_question:
    st.success(
        "AI Response:\n\n"
        "Based on current trends and inventory levels, the risk status is derived "
        "from predicted demand exceeding available stock. Acting early can prevent losses."
    )

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("Hackathon Project | Generative AI Supply Chain System")
