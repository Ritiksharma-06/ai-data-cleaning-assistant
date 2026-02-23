import datetime

class ReportGenerator:

    @staticmethod
    def generate(report):

        text = f"DATA CLEANING REPORT\n"
        text += f"Generated: {datetime.datetime.now()}\n\n"

        for key, value in report.items():

            text += f"{key}:\n"
            text += f"{value}\n\n"

        return text