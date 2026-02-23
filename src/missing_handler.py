import pandas as pd

class MissingValueHandler:

    @staticmethod
    def handle(df):

        report = {}
        total_missing = df.isnull().sum().sum()

        for column in df.columns:

            missing_count = df[column].isnull().sum()

            if missing_count > 0:

                if df[column].dtype == "object":

                    fill_value = df[column].mode()[0]
                    df[column].fillna(fill_value, inplace=True)

                else:

                    fill_value = df[column].median()
                    df[column].fillna(fill_value, inplace=True)

                report[column] = int(missing_count)

        return df, report, int(total_missing)