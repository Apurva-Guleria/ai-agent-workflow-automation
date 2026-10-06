import pandas as pd


class CSVTool:

    def read_csv(self, file_path):
        return pd.read_csv(file_path)