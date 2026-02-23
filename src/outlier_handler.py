import pandas as pd
import numpy as np

class OutlierHandler:

    @staticmethod
    def handle(df):

        report = {}
        total_outliers = 0

        exclude_columns = [
            "id",
            "zipcode",
            "lat",
            "long",
            "yr_built",
            "yr_renovated",
            "waterfront",
            "view",
            "condition",
            "grade",
            "floors"
        ]

        numeric_columns = df.select_dtypes(
            include=['int64','float64']
        ).columns

        numeric_columns = [
            col for col in numeric_columns
            if col not in exclude_columns
        ]

        for column in numeric_columns:

            # Skip low unique columns
            if df[column].nunique() < 30:
                report[column] = "Skipped (categorical numeric)"
                continue

            # Apply log transform if skewed
            skewness = df[column].skew()

            temp = df[column].copy()

            if skewness > 1:
                temp = np.log1p(temp)

            lower = temp.quantile(0.01)
            upper = temp.quantile(0.99)

            outliers = ((temp < lower) | (temp > upper)).sum()

            total_outliers += outliers

            # Apply clipping
            clipped = temp.clip(lower, upper)

            # Reverse log transform
            if skewness > 1:
                clipped = np.expm1(clipped)

            df[column] = clipped

            report[column] = int(outliers)

        return df, report, int(total_outliers)