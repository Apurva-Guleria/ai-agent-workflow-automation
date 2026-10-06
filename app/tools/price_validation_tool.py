import pandas as pd
from app.tools.calculator import Calculator


class PriceValidationTool:

    def __init__(self):
        self.calculator = Calculator()

    def find_price_differences(
        self,
        file_path,
        threshold=10
    ):

        data = pd.read_csv(file_path)

        data["percentage_difference"] = data.apply(
            lambda row: self.calculator.percentage_difference(
                row["our_price"],
                row["vendor_price"]
            ),
            axis=1
        )

        differences = data[
            data["percentage_difference"] > threshold
        ].copy()

        return differences