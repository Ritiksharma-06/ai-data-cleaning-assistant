import streamlit as st
import pandas as pd
import os

from src.data_loader import DataLoader
from src.cleaning_pipeline import CleaningPipeline


# Page config
st.set_page_config(
    page_title="AI Data Cleaning Assistant",
    layout="wide"
)

# Title
st.title("AI-Powered Data Cleaning Assistant")

st.write("Upload CSV or Excel file for automatic cleaning")


# File uploader
uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx"]
)


if uploaded_file:

    # Load dataset
    df = DataLoader.load(uploaded_file)

    original_df = df.copy()

    # Raw preview
    st.subheader("Raw Dataset Preview")

    st.dataframe(df.head(), use_container_width=True)

    st.write("Shape:", df.shape)


    # Run cleaning button
    if st.button("Run AI Cleaning"):

        cleaned_df, report, report_text = CleaningPipeline.run(df)


        # Cleaned preview
        st.subheader("Cleaned Dataset Preview")

        st.dataframe(cleaned_df.head(), use_container_width=True)

        st.write("Cleaned Shape:", cleaned_df.shape)


        # Cleaning summary
        st.subheader("Cleaning Summary")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Missing Fixed",
            report["Total Missing"]
        )

        col2.metric(
            "Outliers Fixed",
            report["Total Outliers"]
        )

        col3.metric(
            "Duplicates Removed",
            report["Duplicates Removed"]
        )


        # Validation report
        st.subheader("Validation Report")

        validation = report["Validation Report"]

        std_df = pd.DataFrame({
            "Column": list(validation["Std Deviation Reduction"].keys()),
            "STD Reduction": list(validation["Std Deviation Reduction"].values())
        })

        var_df = pd.DataFrame({
            "Column": list(validation["Variance Reduction %"].keys()),
            "Variance Reduction %": list(validation["Variance Reduction %"].values())
        })

        col1, col2 = st.columns(2)

        with col1:
            st.write("Standard Deviation Reduction")
            st.dataframe(std_df, use_container_width=True)

        with col2:
            st.write("Variance Reduction (%)")
            st.dataframe(var_df, use_container_width=True)


        # Detailed report
        st.subheader("Detailed Report")

        st.text(report_text)


        # Save cleaned dataset and report
        os.makedirs("data/cleaned", exist_ok=True)
        os.makedirs("reports", exist_ok=True)

        cleaned_df.to_csv(
            "data/cleaned/cleaned_data.csv",
            index=False
        )

        with open("reports/report.txt", "w") as f:
            f.write(report_text)


        st.success("Cleaned dataset and report saved successfully")


        # Download cleaned dataset
        csv = cleaned_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Cleaned CSV",
            data=csv,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )


        # Before vs After comparison example
        if "price" in original_df.columns:

            st.subheader("Before vs After Comparison (price column)")

            col1, col2 = st.columns(2)

            col1.metric(
                "Original Price STD",
                round(original_df["price"].std(), 2)
            )

            col2.metric(
                "Cleaned Price STD",
                round(cleaned_df["price"].std(), 2)
            )