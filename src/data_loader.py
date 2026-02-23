import pandas as pd

class DataLoader:

    @staticmethod
    def load(file):

        try:
            if file.name.endswith(".csv"):
                df = pd.read_csv(file)

            elif file.name.endswith(".xlsx"):
                df = pd.read_excel(file)

            else:
                raise Exception("Unsupported format")

            return df

        except Exception as e:
            raise Exception(f"Error loading file: {e}")