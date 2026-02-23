from src.missing_handler import MissingValueHandler
from src.outlier_handler import OutlierHandler
from src.duplicate_handler import DuplicateHandler
from src.datatype_handler import DataTypeHandler
from src.report_generator import ReportGenerator

import pandas as pd


class CleaningPipeline:

    @staticmethod
    def validate_cleaning(original_df, cleaned_df):
        """
        Validate improvement in data quality by comparing
        standard deviation before and after cleaning.
        """

        validation_report = {}

        numeric_cols = original_df.select_dtypes(
            include=['int64', 'float64']
        ).columns

        std_reduction = {}
        variance_reduction_percent = {}

        for col in numeric_cols:

            original_std = float(original_df[col].std())
            cleaned_std = float(cleaned_df[col].std())

            reduction = original_std - cleaned_std

            if original_std != 0:
                percent_reduction = (reduction / original_std) * 100
            else:
                percent_reduction = 0.0

            # convert to normal float and round
            std_reduction[col] = round(float(reduction), 2)
            variance_reduction_percent[col] = round(float(percent_reduction), 2)

        validation_report["Std Deviation Reduction"] = std_reduction
        validation_report["Variance Reduction %"] = variance_reduction_percent

        return validation_report


    @staticmethod
    def run(df):
        """
        Complete cleaning pipeline
        """

        # Save original dataset for validation
        original_df = df.copy()

        report = {}

        # Step 1: Missing values
        df, missing_report, total_missing = MissingValueHandler.handle(df)

        report["Missing Values Fixed"] = missing_report
        report["Total Missing"] = total_missing

        # Step 2: Outliers
        df, outlier_report, total_outliers = OutlierHandler.handle(df)

        report["Outliers Fixed"] = outlier_report
        report["Total Outliers"] = total_outliers

        # Step 3: Duplicates
        df, duplicates_removed = DuplicateHandler.handle(df)

        report["Duplicates Removed"] = duplicates_removed

        # Step 4: Datatype correction
        df, datatype_report = DataTypeHandler.handle(df)

        report["Data Types"] = datatype_report

        # Step 5: Validation
        validation_report = CleaningPipeline.validate_cleaning(
            original_df,
            df
        )

        report["Validation Report"] = validation_report

        # Step 6: Generate text report
        report_text = ReportGenerator.generate(report)

        return df, report, report_text