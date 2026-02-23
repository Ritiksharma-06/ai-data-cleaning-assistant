class DuplicateHandler:

    @staticmethod
    def handle(df):

        before = len(df)

        df = df.drop_duplicates()

        after = len(df)

        removed = before - after

        return df, int(removed)