import pandas as pd

class DataTypeHandler:

    @staticmethod
    def handle(df):

        report = {}

        for column in df.columns:

            try:

                df[column] = pd.to_numeric(df[column])

                report[column] = "Numeric"

            except:

                report[column] = "Categorical"

        return df, report