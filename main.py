import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="BudgetGenie AI",  layout="centered")

st.title("BudgetGenie AI")
st.subheader("Smart Budget-Based Product Recommender")

# Load dataset
df = pd.read_csv(r"C:\AI Agent\budget genie AI\budgetgenie_products.csv")

# User inputs
budget = st.number_input("Enter Your Budget", min_value=0.0, step=10.0)
country = st.selectbox("Select Your Country", df["country"].unique())

# Button
if st.button("Find Products 🔍"):

    filtered = df[(df["country"] == country) & (df["price"] <= budget)]

    if filtered.empty:
        st.warning("No products found under your budget.")
    else:
        filtered = filtered.copy()
        filtered["trend_score"] = filtered["rating"] * np.log(filtered["reviews"])

        top_products = filtered.sort_values(by="trend_score", ascending=False).head(3)

        st.success("Top Recommended Products For You:")

        for index, row in top_products.iterrows():
            st.markdown("---")
            st.write(f"### {row['name']}")
            st.write(f"Price: {row['price']}")
            st.write(f"Rating: {row['rating']}")
